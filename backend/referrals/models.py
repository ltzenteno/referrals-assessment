import uuid
from django.db import models
from django.utils import timezone


class Referral(models.Model):

    class Status(models.TextChoices):
        INVITATION_SENT = "invitation_sent", "Invitation Sent"
        APPLICATION_RECEIVED = "application_received", "Application Received"
        JOINED = "joined", "Joined"
        DECLINED = "declined", "Declined"

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.INVITATION_SENT)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_sent_at = models.DateTimeField()

    def save(self, *args, **kwargs) -> None:
        self.email = self.email.strip().lower()

        super().save(*args, **kwargs)

    def rotate_token(self) -> None:
        """
        Rotates the token and updates last_sent_at to current time
        """
        self.token = uuid.uuid4()
        self.last_sent_at = timezone.now()
        self.save()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.email}"
