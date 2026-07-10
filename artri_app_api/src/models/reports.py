from django.db import models

from .accounts import User
from .exercises import Training


class TrainingReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.training.name} - {self.date}'


class DailyPainReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    pain_level = models.IntegerField()  # 0-10
    pain_location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} - {self.date}'


class DailySleepReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    sleep_duration = models.IntegerField()  # in hours
    sleep_quality = models.CharField(max_length=50)  # e.g., 'Good', 'Fair', 'Poor'

    def __str__(self):
        return f'{self.user.username} - {self.date}'


class DailySwellingReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    swelling_level = models.IntegerField()  # 0-10
    swelling_location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} - {self.date}'


class DailyFatigueReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    fatigue_level = models.IntegerField()  # 0-10
    fatigue_description = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.date}'
