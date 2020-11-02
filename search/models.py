from django.db import models

# Create your models here.
REGION = [
    ("One", 1),
    ("Two", 2),
    ("Three", 3),
    ("Four", 4)
]

class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100, choices=REGION, default="One")
    population = models.IntegerField()

    class Meta:
        verbose_name = 'Cities'

    def __str__(self):
        return self.name



