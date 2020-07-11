from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    code = models.CharField(max_length=120, blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
