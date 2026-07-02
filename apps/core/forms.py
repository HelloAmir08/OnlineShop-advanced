from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields  = ['first_name', 'second_name', 'phone_number', 'subject', 'message']