from django.urls import path
from .views import (login_view, logout_view, password_change_view, profile_edit_view, profile_view, register_view,
)

urlpatterns = [
    path('registration/', register_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/password/', password_change_view, name='password_change'),
]
