from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    """Band means group."""
    title = models.CharField(max_length=10)
    started = models.DateField(blank=True)


# class Student(User):
#     pass
