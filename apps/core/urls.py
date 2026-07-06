from django.urls import path
from .views import about_us_view, contact_us_view

urlpatterns = [
    path('about-us/', about_us_view, name = 'about_us'),
    path('contact_us/', contact_us_view, name = 'contact_us')
]