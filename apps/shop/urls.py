from django.urls import path
from .views import homepage_view, product_detail_view
urlpatterns = [
    path('', homepage_view, name='home' ),
    path('product_details/<int:pk>/', product_detail_view, name='product_detail'),
]