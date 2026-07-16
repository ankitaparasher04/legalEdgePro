from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Case(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_cases')
    lawyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lawyer_cases')
    
    title = models.CharField(max_length=200)
    description = models.TextField()

    status = models.CharField(max_length=20, default='active')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class CaseNote(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.case.title}"