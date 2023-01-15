from django.db import models
from ckeditor.fields import RichTextField


class Task(models.Model):
    HOMEWORK_NUMBER_CHOICES = [
        (1, 1), (2, 2), (3, 3), (4, 4),
        (5, 5), (6, 6), (7, 7), (8, 8)
    ]
    number = models.PositiveSmallIntegerField(choices=HOMEWORK_NUMBER_CHOICES, default=1)
    content = RichTextField()
    deadline = models.DateTimeField()
    is_active = models.BooleanField(default=False)
