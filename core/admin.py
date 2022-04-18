# ** Django Imports **
from django.contrib import admin

# ** App Imports **
from core.models import Commission


@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'flat', 'city', 'net_incoming', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('reservation', 'flat', 'city')
    readonly_fields = ('created_at', 'updated_at')
