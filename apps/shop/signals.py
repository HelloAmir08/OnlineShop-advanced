from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, ProductImage

@receiver(post_save, sender = Product)
def set_default_image(sender, instance, created, **kwargs):
    if created:
        ProductImage.objects.create(product=instance)