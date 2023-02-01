from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from tasks.models import Task
from django.views.generic.list import ListView
from students.models import Student

def index(request):
    user = Student.objects.create(username='py_student_3', password='A123456b', band_id=2)
    return render(request, user)
    # return render(request, 'tasks/tasks.html', {'Tasks': Task.objects.filter(is_active=True).order_by('number')})



# class TasksListView(ListView):
#     model = Task
