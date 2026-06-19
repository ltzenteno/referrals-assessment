from rest_framework import serializers
from django.utils import timezone

from referrals.exceptions import EmailAlreadyExistsError
from referrals.models import Referral


class ReferralCreateSerializer(serializers.ModelSerializer[Referral]):
    first_name = serializers.CharField(max_length=150, allow_blank=False, trim_whitespace=True)
    last_name = serializers.CharField(max_length=150, allow_blank=False, trim_whitespace=True)
    email = serializers.EmailField(validators=[]) # removing auto generated UniqueValidator and instead validate with validate_email method

    class Meta:
        model = Referral
        fields = ["first_name", "last_name", "email"]

    def validate_email(self, value: str) -> str:
        normalized_email = value.strip().lower()

        if Referral.objects.filter(email=normalized_email).exists():
            raise EmailAlreadyExistsError()

        return normalized_email

    def create(self, validated_data: dict) -> Referral:
        validated_data["last_sent_at"] = timezone.now()
        return super().create(validated_data)


class ReferralSerializer(serializers.ModelSerializer[Referral]):
    class Meta:
        model = Referral
        fields = ["id", "first_name", "last_name", "email", "status", "created_at", "last_sent_at"]


class ReferralTokenLookupSerializer(serializers.ModelSerializer[Referral]):
    class Meta:
        model = Referral
        fields = ["id", "first_name", "last_name", "email", "status"]
