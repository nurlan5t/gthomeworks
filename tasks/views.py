from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from tasks.forms import CreateHomeworkForm
from students.models import Student


class TasksListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        """Return all active Tasks"""
        current_student = Student.objects.get(id=self.request.user.pk)
        return Task.objects.filter(
            is_active=True,
            bands=current_student.band).order_by('-deadline').exclude(homework__student=current_student)


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            homework_form = CreateHomeworkForm(request.POST, request.FILES)
            if homework_form.is_valid():
                new_hw = homework_form.save(commit=False)
                new_hw.student = Student.objects.get(pk=request.user.pk)
                new_hw.task = self.get_object()
                new_hw.save()
                return redirect(f'/')
        else:
            homework_form = CreateHomeworkForm(instance=request.user)
        return render(request, self.template_name, {'task': self.template_name, 'homework_form': homework_form})
