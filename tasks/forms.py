from django import forms
from django.core.validators import FileExtensionValidator
from tasks.models import Homework


class CreateHomeworkForm(forms.ModelForm):
    file = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(['py'])],
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    link_to_git = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
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
        fields = ('file', 'link_to_git', 'stand_up')
