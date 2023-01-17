from django.contrib import admin
from students.models import Band


@admin.register(Band)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "started")
