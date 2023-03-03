from django.contrib import admin
from tasks.models import Task, Homework


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("number", "deadline", "is_active", "bands")

    @admin.display()
    def bands(self, obj):
        return obj.task.bands


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ("task_number", "student_fullname", "created", "group_number", "is_deadline", "is_checked")

    @admin.display()
    def task_number(self, obj):
        return obj.task.number

    @admin.display()
    def student_fullname(self, obj):
        return obj.student.get_full_name()

    @admin.display()
    def group_number(self, obj):
        return obj.student.band.group_number
