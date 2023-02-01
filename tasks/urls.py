from django.urls import path

from tasks.views import index

urlpatterns = [
    path('tasks/', index, name='index'),
]