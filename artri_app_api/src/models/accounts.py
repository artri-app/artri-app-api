from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)

    def __str__(self):
        return self.username
