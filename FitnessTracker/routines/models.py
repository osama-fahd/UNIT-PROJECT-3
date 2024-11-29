from django.db import models

class Routine(models.Model):
    name = models.CharField(max_length=256)
    all_weights = models.PositiveBigIntegerField(blank=True)
    