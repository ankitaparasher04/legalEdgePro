from django.db import models
from accounts.models import User
from clients.models import Client


class Case(models.Model):

    CASE_STATUS = (
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("closed", "Closed"),
        ("on_hold", "On Hold"),
    )

    CASE_TYPES = (
        ("civil", "Civil"),
        ("criminal", "Criminal"),
        ("corporate", "Corporate"),
        ("family", "Family"),
        ("property", "Property"),
        ("other", "Other"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="cases"
    )

    lawyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'lawyer'},
        related_name="assigned_cases"
    )

    case_type = models.CharField(max_length=50, choices=CASE_TYPES)
    status = models.CharField(max_length=20, choices=CASE_STATUS, default="open")

    court_name = models.CharField(max_length=200, blank=True)
    hearing_date = models.DateField(blank=True, null=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.client.full_name}"