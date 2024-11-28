from django.db import models
from django.contrib.auth.models import User
from exercises.models import Exercise

class Workout(models.Model):
    exercise = models.OneToOneField(Exercise, on_delete=models.CASCADE)
    note = models.TextField(blank=True)
    restTime = models.PositiveIntegerField(blank=True)
    

class Set(models.Model):
    weight = models.FloatField()
    repetition = models.PositiveIntegerField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
