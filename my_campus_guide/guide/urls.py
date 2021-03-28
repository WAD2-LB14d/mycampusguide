from django.urls import path
from guide import views

app_name = 'guide'

urlpatterns = [
  path('', views.index, name='index'),
  path('courses/', views.courses, name='courses'),
  path('lecturers/', views.lecturers, name='lecturers'),
  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('courses/add_course/', views.add_course, name='add_course'),
  path('lecturers/add_lecturer/', views.add_lecturer, name='add_lecturer'),
  path('lecturers/<slug:lecturer_name_slug>/', views.show_lecturer, name = "show_lecturer"),
]
