from django.urls import path
from tasks.views import TasksListView, TaskDetailView

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
]
