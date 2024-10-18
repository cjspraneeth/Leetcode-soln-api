from django.db import models

class Problem(models.Model):
    number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    link = models.URLField()
    time_complexity = models.CharField(max_length=100)
    space_complexity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.number}: {self.name}"