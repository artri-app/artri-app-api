from django.db import models

from .accounts import User
from .common import DAYS_OF_WEEK


class Remedy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    days_of_week = models.CharField(choices=DAYS_OF_WEEK, max_length=9, default='Monday')
    hour = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
