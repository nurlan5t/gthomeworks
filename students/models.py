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
        return f'{self.title} {self.group_number} m{self.month}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы студентов'


class Student(User):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.username:
            self.set_password(self.password)
            super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.get_full_name()} ({self.band})'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
