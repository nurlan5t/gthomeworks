from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.timezone import localtime
from ckeditor.fields import RichTextField
from students.models import Student, Band
from .functions import gen_number_choices
from django.core.files.storage import FileSystemStorage


class Task(models.Model):
    TASK_NUMBER_CHOICES = gen_number_choices(max_value=8)
    number = models.PositiveSmallIntegerField(choices=TASK_NUMBER_CHOICES, default=1)
    content = RichTextField()
    deadline = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    topic = models.CharField(max_length=255, blank=True, null=True)
    bands = models.ManyToManyField(Band)

    def __str__(self):
        return str(self.number)


class Homework(models.Model):
    # student's input data
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    file = models.FileField(null=True, blank=True, upload_to='uploads/', max_length=100,
                            validators=[FileExtensionValidator(['py'])])
    link_to_git = models.URLField(null=True, blank=True, max_length=255)
    stand_up = models.TextField()

    # auto save data
    created = models.DateTimeField(default=localtime)
    is_deadline = models.BooleanField(default=False, blank=True)

    # teacher's input data
    HOMEWORK_RATE_CHOICES = gen_number_choices(max_value=10)
    score = models.PositiveSmallIntegerField(choices=HOMEWORK_RATE_CHOICES, default=1, blank=True)
    feedback = RichTextField(blank=True)
    is_checked = models.BooleanField(default=False, blank=True)

    def save(self, *args, **kwargs):
        if self.is_checked:
            FileSystemStorage().delete(str(self.file))
            if self.student.email:
                send_mail(
                    subject=f'Домашнее Задание №{self.task.number}',
                    message=f'Оценка: {self.score} из 10\n\n'
                            f'подробнее: http://127.0.0.1:8000/my_homeworks/',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[f'{self.student.email}'],
                )
        if self.created.__le__(self.task.deadline):
            self.is_deadline = True
        else:
            self.is_deadline = False
        super(Homework, self).save(*args, **kwargs)


@receiver(post_delete, sender=Homework)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old HW file """
    try:
        instance.file.delete(save=False)
    except:
        pass