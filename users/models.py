from django.db import models

# Create your models here.

# import abstract user
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    # now go to the forms file and import CustomUser