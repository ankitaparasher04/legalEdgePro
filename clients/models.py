from django.db import models
from accounts.models import User

class Client(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('blacklisted', 'Blacklisted'),
    )

    # Basic Info
    lawyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='clients',
        limit_choices_to={'role': 'lawyer'}
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active')

    # Documents
    profile_picture = models.ImageField(upload_to='clients/photos/', blank=True, null=True)
    id_document = models.FileField(upload_to='clients/documents/', blank=True, null=True)

    # Notes
    notes = models.TextField(blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class ConflictCheck(models.Model):
    STATUS_CHOICES = (
        ('clear', 'Clear'),
        ('conflict', 'Conflict'),
        ('pending', 'Pending'),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='conflict_checks')
    checked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conflict Check - {self.client.full_name} - {self.status}"