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
class Products(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)

# class Enrollment(models.Model):
#     student = models.ForeignKey('Student', on_delete=models.CASCADE)
#     course = models.ForeignKey('Course', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         unique_together = ('student', 'course')

