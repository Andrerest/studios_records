from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    firstName = models.CharField(max_length=50, blank=False, default="")
    lastName = models.CharField(max_length=50, blank=False, default="")
    bio = models.CharField(max_length=196, default="")
    created = models.DateTimeField(default=timezone.now)