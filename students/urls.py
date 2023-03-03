from django.contrib.auth.views import LogoutView
from django.urls import path
from students.views import LoginUser, StudentDetailView, StudentHomeworksView

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('user/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('homeworks/', StudentHomeworksView.as_view(), name='student-homeworks'),
]
