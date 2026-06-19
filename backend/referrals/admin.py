from django.contrib import admin

from referrals.models import Referral


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ("__str__", "status", "created_at", "last_sent_at",)
    list_filter = ("status",)
    search_fields = ("email", "first_name", "last_name",)
    readonly_fields = ("token", "created_at", "last_sent_at",)
