import time
from django.utils import timezone
from .models import Referral
from .exceptions import EmailAlreadyExistsError


class ReferralService:

    @staticmethod
    def create_referral(first_name: str, last_name: str, email: str) -> Referral:
        normalized_email = email.strip().lower()
        if Referral.objects.filter(email=normalized_email).exists():
            raise EmailAlreadyExistsError()

        return Referral.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=normalized_email,
            last_sent_at=timezone.now(),
        )

    @staticmethod
    def resend_invitation(referral: Referral) -> Referral:
        if referral.status != Referral.Status.INVITATION_SENT:
            raise ValueError("Can only resend invitations with status 'Invitation Sent'.")

        seconds_since_last: float = (timezone.now() - referral.last_sent_at).total_seconds()
        if seconds_since_last < 30:
            raise ValueError("Cannot resend within 30 seconds.")

        time.sleep(0.5) # simulate email sending delay
        referral.rotate_token()

        return referral

    # For assessment scope, tokens do not have a time-based expiry. They are single-purpose:
    # a token stops working once the referral status advances past 'invitation_sent'.
    @staticmethod
    def lookup_by_token(token: str) -> Referral:
        try:
            referral = Referral.objects.get(token=token)
        except Referral.DoesNotExist:
            raise Referral.DoesNotExist

        if referral.status != Referral.Status.INVITATION_SENT:
            raise PermissionError("This token has already been used.")

        return referral

    @staticmethod
    def get_analytics() -> dict:
        total: int = Referral.objects.count()
        invitations_sent: int = Referral.objects.filter(status=Referral.Status.INVITATION_SENT).count()
        joined: int = Referral.objects.filter(status=Referral.Status.JOINED).count()
        if total > 0:
            conversion_rate: float = round((joined / total * 100), 2)
        else:
            conversion_rate = 0.0
        return {
            "total_invited": total,
            "invitations_sent": invitations_sent,
            "joined": joined,
            "conversion_rate": conversion_rate,
        }