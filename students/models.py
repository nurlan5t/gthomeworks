from django.db import models
from django.contrib.auth.models import User
from tasks.functions import gen_number_choices


class Band(models.Model):
    """Band means student group."""
    MONTH_NUMBER_CHOICES = gen_number_choices(max_value=12)
    title = models.CharField(max_length=15)
    group_number = models.CharField(max_length=10, null=True, unique=True)
    started = models.DateField(blank=True)
    month = models.PositiveSmallIntegerField(choices=MONTH_NUMBER_CHOICES, default=1)

    def __str__(self):
        return f'{self.group_number} m{self.month}'


class Student(User):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.band.group_number}'

    class Meta:
        verbose_name = 'Student'
