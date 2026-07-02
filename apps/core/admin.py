from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "phone_number",
        "subject",
        "created_at"
    ]
    list_filter = ["status", "created_at"]
    search_fields = ["first_name", "phone_number", "subject"]
    ordering = ["-created_at"]

