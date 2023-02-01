from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    """Band means group."""
    title = models.CharField(max_length=15)
    group_number = models.CharField(max_length=10, null=True)
    started = models.DateField(blank=True)


class Student(User):
    band = models.ForeignKey(Band, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Student'
