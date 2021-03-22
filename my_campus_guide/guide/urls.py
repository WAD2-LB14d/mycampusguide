from django.urls import path
from guide import views

app_name = 'guide'

urlpatterns = [
  path('', views.index, name='index'),
  path('courses/', views.courses, name='courses'),
  path('lecturers/', views.lecturers, name='lecturers'),
]
