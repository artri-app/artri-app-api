from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)

    def __str__(self):
        return self.email
    
class remedy(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Segunda-feira'),
        ('Tuesday', 'Terça-feira'),
        ('Wednesday', 'Quarta-feira'),
        ('Thursday', 'Quinta-feira'),
        ('Friday', 'Sexta-feira'),
        ('Saturday', 'Sábado'),
        ('Sunday', 'Domingo')
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    days_of_week = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    hour = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    