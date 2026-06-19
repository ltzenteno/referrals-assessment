from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.serializers import BaseSerializer

from referrals.models import Referral
from referrals.serializers import ReferralCreateSerializer, ReferralSerializer
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