from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import PasswordChangeForm
from .models import User, Profile
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone_number', 'email', 'first_name', 'last_name', 'password1', 'password2' )

class LoginForm(forms.Form):
    phone_number = PhoneNumberField(
        required = True,
        region = "UZ",
    )
    password = forms.CharField(
        required = True,
        widget = forms.PasswordInput()
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'birthday', 'address')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'avatar': 'Avatar',
            'birthday': 'Birthday',
            'address': 'Address',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number', 'email', 'first_name', 'last_name')
        labels = {
            'phone_number': 'Phone number',
            'email': 'Email',
            'first_name': 'First name',
            'last_name': 'Last name',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = 'Current password'
        self.fields['new_password1'].label = 'New password'
        self.fields['new_password2'].label = 'Confirm password'
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')
