from django.db import models
from ckeditor.fields import RichTextField
from students.models import Student
from django.core.validators import FileExtensionValidator, MinLengthValidator


def gen_number_choices(max_value: int) -> tuple:
    return tuple(enumerate(range(1, (max_value + 1)), start=1))


class Task(models.Model):
    TASK_NUMBER_CHOICES = gen_number_choices(max_value=8)
    number = models.PositiveSmallIntegerField(choices=TASK_NUMBER_CHOICES, default=1)
    content = RichTextField()
    deadline = models.DateTimeField()
    is_active = models.BooleanField(default=False)


class Homework(models.Model):
    HOMEWORK_RATE_CHOICES = gen_number_choices(max_value=10)
    # student's input data
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    file = models.FileField(upload_to='uploads/', max_length=100, validators=[FileExtensionValidator(['py'])])
    stand_up = models.TextField(MinLengthValidator(60))
    # auto saved data
    created = models.DateTimeField(auto_now_add=True)
    is_deadline = models.BooleanField(default=False, blank=True)
    status = models.BooleanField(default=False, blank=True)
    # teacher's input data
    score = models.PositiveSmallIntegerField(choices=HOMEWORK_RATE_CHOICES, default=1, blank=True)
    feedback = RichTextField(blank=True)
