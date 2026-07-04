from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from apps.core.models import BaseModel
from .managers import UserManager

class User(AbstractUser):
    username = None
    phone_number = PhoneNumberField(
        region = "UZ",
        unique = True
    )
    email = models.EmailField(
        blank = True,
        null = True
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.phone_number.as_e164

class Profile(BaseModel):
    avatar = models.ImageField(
        upload_to='profile_image/',
        blank = True,
        null = True,
        default= 'profile_image/avatar-default.svg'
    )
    birthday = models.DateField(
        blank=True,
        null = True
    )
    address = models.TextField(
        blank = True,
        null = True
    )
    user = models.OneToOneField(
        User,
        on_delete = CASCADE,
        related_name = 'profile'
    )

    def __str__(self):
        return f'{self.user.phone_number} - Profile'

