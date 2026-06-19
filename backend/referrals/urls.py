from django.urls import path, include
from rest_framework.routers import DefaultRouter

from referrals.views import ReferralViewSet, analytics

router = DefaultRouter()
router.register(r'', ReferralViewSet, basename='referral')

urlpatterns = [
    path('analytics/', analytics),
    path('', include(router.urls)),
]
