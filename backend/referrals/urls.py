from django.urls import path, include
from rest_framework.routers import DefaultRouter

from referrals.views import ReferralViewSet

router = DefaultRouter()
router.register(r'', ReferralViewSet, basename='referral')

urlpatterns = [
    path('', include(router.urls)),
]
