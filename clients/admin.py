from django.contrib import admin
from django.utils.html import format_html
from .models import Client, ConflictCheck


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "email",
        "phone",
        "lawyer",
        "status_badge",
        "created_at",
    )

    list_filter = (
        "status",
        "gender",
        "lawyer",
        "created_at",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "profile_preview",
    )

    ordering = ("-created_at",)

    # Status color badge
    def status_badge(self, obj):
        if obj.status == "active":
            color = "green"
        elif obj.status == "inactive":
            color = "orange"
        else:
            color = "red"

        return format_html(
            '<span style="color:{}; font-weight:bold;">{}</span>',
            color,
            obj.status.upper(),
        )

    status_badge.short_description = "Status"

    # Profile image preview
    def profile_preview(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" width="80" style="border-radius:50%;" />',
                obj.profile_picture.url
            )
        return "No Image"

    profile_preview.short_description = "Profile Picture"


@admin.register(ConflictCheck)
class ConflictCheckAdmin(admin.ModelAdmin):

    list_display = (
        "client",
        "checked_by",
        "status_badge",
        "checked_at",
    )

    list_filter = (
        "status",
        "checked_at",
    )

    search_fields = (
        "client__first_name",
        "client__last_name",
    )

    ordering = ("-checked_at",)

    def status_badge(self, obj):
        if obj.status == "clear":
            color = "green"
        elif obj.status == "conflict":
            color = "red"
        else:
            color = "orange"

        return format_html(
            '<span style="color:{}; font-weight:bold;">{}</span>',
            color,
            obj.status.upper(),
        )

    status_badge.short_description = "Status"