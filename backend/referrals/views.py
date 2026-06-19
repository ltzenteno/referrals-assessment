from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.request import Request

from referrals.models import Referral
from referrals.serializers import ReferralCreateSerializer, ReferralSerializer, ReferralTokenLookupSerializer
from referrals.services import ReferralService


class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all().order_by('-created_at')
    serializer_class = ReferralSerializer

    def create(self, request: Request) -> Response:
        write_serializer = ReferralCreateSerializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        referral = ReferralService.create_referral(**write_serializer.validated_data)

        return Response(ReferralSerializer(referral).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def resend(self, request: Request, pk: int | None = None) -> Response:
        """
        Resend an invitation and rotates the token
        """
        referral: Referral = self.get_object()

        try:
            referral = ReferralService.resend_invitation(referral)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

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
            referral = ReferralService.lookup_by_token(token)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Referral.DoesNotExist:
            return Response({"detail": "Invalid or Expired token."}, status=status.HTTP_404_NOT_FOUND)
        except PermissionError:
            return Response({"detail": "This token has already been used."}, status=status.HTTP_410_GONE)

        return Response(ReferralTokenLookupSerializer(referral).data, status=status.HTTP_200_OK)



# using api_view instead of creating another viewset for only 1 endpoint
@api_view(['GET'])
def analytics(request: Request) -> Response:
    return Response(ReferralService.get_analytics())