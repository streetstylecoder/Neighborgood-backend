from django.db import models

class user_info(models.Model):
    # Assuming 'id' is automatically added by Django as a primary key
    person = models.CharField(max_length=200, null=False)
    age = models.IntegerField(null=False)
    email = models.EmailField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=120, null=False, unique=True)
    walking = models.CharField(max_length=200, null=False)
    running = models.CharField(max_length=200, null=False)
    gardening = models.CharField(max_length=200, null=True, blank=True)
    swim = models.CharField(max_length=200, null=False)
    tea = models.CharField(max_length=200, null=True, blank=True)
    like = models.CharField(max_length=200, null=True, blank=True)
    tv = models.CharField(max_length=200, null=True, blank=True)
    movie = models.CharField(max_length=200, null=True, blank=True)
    shopping = models.CharField(max_length=200, null=True, blank=True)
    happy = models.CharField(max_length=200, null=True, blank=True)
    errands = models.CharField(max_length=200, null=True, blank=True)  # Note: Corrected spelling from 'erands' to 'errands'
    rides = models.CharField(max_length=200, null=True, blank=True)
    childcare = models.CharField(max_length=200, null=True, blank=True)
    eldercare = models.CharField(max_length=200, null=True, blank=True)
    petcare = models.CharField(max_length=200, null=True, blank=True)
    tutoring = models.CharField(max_length=200, null=True, blank=True)
    home = models.CharField(max_length=200, null=True, blank=True)
    landscape = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)  # Nullable as no constraint was specified
    longitude = models.FloatField(null=True, blank=True)  # Nullable as no constraint was specified
    sharePreference = models.CharField(max_length=200, null=True, blank=True)  # Nullable as no constraint was specified
