from django.db import models

# Create your models here.
from django.db import models

class Faction(models.Model):
    ALIGNMENT_CHOICES = [
        ('neutral', 'Neutral'),
        ('friendly', 'Friendly'),
        ('hostile', 'Hostile'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    alignment = models.CharField(max_length=20, choices=ALIGNMENT_CHOICES)

    def __str__(self):
        return self.name
