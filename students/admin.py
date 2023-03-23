from django.contrib import admin
from students.models import Band, Student
from tasks.models import Homework


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('title', 'group_number', 'started', 'month')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'band_title', 'band_group_number', 'stand_up_count')
    list_filter = ('band',)

    @admin.display(ordering='band__group_number')
    def band_title(self, obj):
        return obj.band.title

    @admin.display()
    def band_group_number(self, obj):
        return obj.band.group_number

    @admin.display()
    def stand_up_count(self, obj):
        counter = Homework.objects.filter(student=obj.student.pk, is_checked=True).count()
        return counter
