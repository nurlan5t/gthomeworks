from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from students.models import Student
from students.forms import UpdateEmailForm
from tasks.models import Homework


class StudentHomeworksView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'tasks/homeworks.html'
    context_object_name = 'homeworks'

    def get_queryset(self):
        return Homework.objects.filter(student=self.request.user.pk)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Student
    context_object_name = 'student'
    template_name = 'tasks/student_detail.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            student_form = UpdateEmailForm(request.POST, instance=request.user)
            if student_form.is_valid():
                student_form.save()
                return redirect(f'/user/{request.user.pk}')
        else:
            student_form = UpdateEmailForm(instance=request.user)
        return render(request, self.template_name, {'student_form': student_form})
