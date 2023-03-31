from django import forms
from students.models import Student, Band
from django.core.validators import FileExtensionValidator, RegexValidator


class UpdateEmailForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ['email']


class CreateStudentsForm(forms.Form):
    band = forms.ModelChoiceField(queryset=Band.objects.all())
    file = forms.FileField(
        validators=[
            FileExtensionValidator(['txt']),
            # RegexValidator(
            #     regex=r'([a-zA-Z_.-]+)_([1-9]+)-([1-9]+)',
            #     message='Название файла должно быть строго по шаблону, например: Python_29-1',
            #     code='invalid_filename'
            # )
        ]
    )
