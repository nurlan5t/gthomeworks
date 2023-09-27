from django import forms
from django.core.validators import FileExtensionValidator
from tasks.models import Homework


class CreateHomeworkForm(forms.ModelForm):
    file = forms.FileField(
        required=True,
        validators=[
            FileExtensionValidator(['py']),
            # RegexValidator(
            #     regex=r'([a-zA-Z_.-]+)_([1-9]+)-([1-9]+)_([a-zA-Z]+[1-8])',
            #     message='Название файла должно быть строго по шаблону, например: Azamat_29-1_hw1',
            #     code='invalid_filename'
            # )
        ],
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        # help_text='Название файла должно быть строго по шаблону, например: Azamat_30-1_hw1
    )
    # link_to_git = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    stand_up = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        min_length=120,
        help_text='#StandUp '
                  '*Что сделал: _____'
                  '*Проблемы: _____'
                  '*Что буду делать: _____'
                  '*Исполнитель: _____'
    )

    class Meta:
        model = Homework
        fields = ('file', 'stand_up')
        # fields = ('file', 'link_to_git', 'stand_up')
