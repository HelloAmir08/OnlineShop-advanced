from django.db import models
from django.db.models import CASCADE
from django.db.models.aggregates import Avg
from apps.core.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.conf import settings


class Category(BaseModel):
    name = models.CharField(
        max_length=200,
        unique=True,
    )

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    name = models.CharField(
        max_length=200,
        unique=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=CASCADE,
        related_name='subcategories'
    )

    def __str__(self):
        return f'{self.category.name} -> {self.name}'


class Product(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    discount = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )
    quantity = models.PositiveIntegerField(default=0)
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=CASCADE,
        related_name='products'
    )

    @property
    def discounted_price(self):
        if self.discount > 0:
            new_price = self.price * (Decimal('100') - Decimal(self.discount)) / Decimal('100')
        else:
            new_price = self.price
        return new_price.quantize(Decimal('0.01'))

    @property
    def first_image(self):
        return self.images.first()

    @property
    def average_rating(self):
        return round(self.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0, 1)

    @property
    def reviews_count(self):
        return self.reviews.count()

    def __str__(self):
        return f'{self.subcategory.name} -> {self.name}'


class ProductImage(BaseModel):
    image = models.ImageField(
        upload_to='product_image/',
        default='product_image/default-photo.webp'
    )
    product = models.ForeignKey(
        Product,
        on_delete=CASCADE,
        related_name='images'
    )

    def __str__(self):
        return f"Image of {self.product.name}"


class Review(BaseModel):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    comment = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    product = models.ForeignKey(
        Product,
        on_delete=CASCADE,
        related_name="reviews"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='reviews',
        blank=True,
        null=True
    )

    @property
    def display_name(self):
        if self.user:
            return self.user.get_full_name()
        elif self.username:
            return self.username
        return self.email

    def __str__(self):
        return f'{self.display_name} - {self.product.name}'



