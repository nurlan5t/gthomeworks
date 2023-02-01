from django.contrib import admin
from students.models import Band, Student


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ("title", "group_number", "started")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "band_title", "band_group_number")

    @admin.display(ordering='band__group_number')
    def band_title(self, obj):
        return obj.band.title

    @admin.display()
    def band_group_number(self, obj):
        return obj.band.group_number
