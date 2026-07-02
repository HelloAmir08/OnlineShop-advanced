from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class ContactMessage(BaseModel):
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In_progress"),
        ("completed", "Completed")
    ]
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(region="UZ")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.phone_number}, status - {self.status}"