import time
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.serializers import BaseSerializer

from referrals.models import Referral
from referrals.serializers import ReferralCreateSerializer, ReferralSerializer, ReferralTokenLookupSerializer


#
# Suggested approach:
# - Use Django REST Framework ViewSets


class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

    def create(self, request: Request) -> Response:
        write_serializer = ReferralCreateSerializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        referral = write_serializer.save()
        response_serializer = ReferralSerializer(referral)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def resend(self, request: Request, pk: int | None = None) -> Response:
        """
        Resend an invitation and rotates the token
        """
        referral: Referral = self.get_object()

        if referral.status != Referral.Status.INVITATION_SENT:
            return Response(
                {"detail": "Can only resend invitations with status 'Invitation Sent'."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        seconds_since_last: float = (timezone.now() - referral.last_sent_at).total_seconds()
        if seconds_since_last < 30:
            return Response(
                {"detail": "Cannot resend within 30 seconds."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        time.sleep(0.5) # simulate email sending delay
        referral.rotate_token()

        return Response(ReferralSerializer(referral).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def lookup(self, request: Request) -> Response:
        """
        Lookup a referral by token
        """
        token: str | None = request.query_params.get("token")

        if not token:
            return Response({"detail": "Token is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            referral = Referral.objects.get(token=token)
        except Referral.DoesNotExist:
            return Response({"detail": "Invalid or Expired token."}, status=status.HTTP_404_NOT_FOUND)

        if referral.status != Referral.Status.INVITATION_SENT:
            return Response({"detail": "This token has already been used."}, status=status.HTTP_410_GONE)

        return Response(ReferralTokenLookupSerializer(referral).data, status=status.HTTP_200_OK)
