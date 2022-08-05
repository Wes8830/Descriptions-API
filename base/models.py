from django.db import models

# Create your models here.


class Columns(models.Model):
    column = models.CharField(max_length=64)
    definition = models.CharField(max_length=512)
    description = models.CharField(max_length=2048)
    # needs to link to Categories
    parentDir = models.CharField(max_length=64) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Categories(models.Model):
    category = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    parentDir = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


# class paColumnDetails(models.Model):


class Sources(models.Model):
    source = models.CharField(max_length=64)
    description = models.CharField(max_length=2048)
    is_real_time = models.BooleanField(default=False)
