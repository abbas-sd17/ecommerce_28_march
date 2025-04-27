from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Abstract base model for common fields
class AuditData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

# Inherit from AuditData
# class Products(AuditData):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     is_available = models.BooleanField(default=False)
#     # created_at = models.DateTimeField(auto_now_add=True)
#

# class Category(models.Model):
#     category_name = models.CharField(max_length=100, primary_key=True)

# class Enrollment(models.Model):
#     student = models.ForeignKey('Student', on_delete=models.CASCADE)
#     course = models.ForeignKey('Course', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         unique_together = ('student', 'course')

# One-to-One Relationship: User Profile Example
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

# Forward access
# profile.user.username
# Reverse access
# user.profile.bio


# One-to-Many Relationship: Category and Products
class Category(models.Model):
    name = models.CharField(max_length=100, default="")

class Products(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    def __str__(self):
        return self.name

# Forward access
# product.category.name
# Reverse access
# category.products.all()

# Many-to-Many Relationship: Order and Products
class Order(models.Model):
    products = models.ManyToManyField(Products, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

# Forward access:
# order.products.all()
# Reverse access:
# product.orders.all()