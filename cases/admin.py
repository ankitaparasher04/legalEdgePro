from django.contrib import admin
from django.utils.html import format_html
from .models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "client",
        "lawyer",
        "case_type",
        "status_badge",
        "hearing_date",
        "created_at",
    )

    list_filter = (
        "case_type",
        "status",
        "lawyer",
        "hearing_date",
    )

    search_fields = (
        "title",
        "client__first_name",
        "client__last_name",
    )

    ordering = ("-created_at",)

    readonly_fields = ("created_at", "updated_at")

    def status_badge(self, obj):

        if obj.status == "open":
            color = "blue"
        elif obj.status == "in_progress":
            color = "orange"
        elif obj.status == "closed":
            color = "green"
        else:
            color = "gray"

        return format_html(
            '<span style="color:{}; font-weight:bold;">{}</span>',
            color,
            obj.status.upper(),
        )

    status_badge.short_description = "Status"