from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from students.models import Student, Band
from students.forms import UpdateEmailForm, CreateStudentsForm
from tasks.models import Homework
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string


class StudentHomeworksView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'tasks/homeworks.html'
    context_object_name = 'homeworks'

    def get_queryset(self):
        return Homework.objects.filter(student=self.request.user.pk).order_by('-created')


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


@login_required
def create_students(request):
    form = CreateStudentsForm(request.POST, request.FILES)
    if request.method == 'POST':
        file = request.FILES['file']
        if form.is_valid():
            fs = FileSystemStorage()
            fs.save(file, file)
            with open(rf'C:\Users\User\PycharmProjects\gthomeworks\media\{str(file)}', encoding='UTF-8') as data:
                students_names_list = data.readlines()
                with open(
                        rf'C:\Users\User\PycharmProjects\gthomeworks\media\Accounts-{str(file)}', 'w',
                        encoding='UTF-8') as profile:
                    for name in students_names_list:
                        new_student = {
                            'first_name': name.strip('\n'),
                            'username': 'geek_' + str(Student.objects.count()+1),
                            'password': get_random_string(10),
                            'band': Band.objects.get(id=form.data.get('band'))
                        }
                        profile.write(f'{new_student}\n')
                        Student(**new_student).save()
            fs.delete(str(file))
            return redirect('/admin/students/student')
    return render(request, 'tasks/students_create.html', {'form': form})
