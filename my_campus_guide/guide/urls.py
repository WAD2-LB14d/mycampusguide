from django.urls import path
from guide import views

app_name = 'guide'

urlpatterns = [
  path('', views.index, name='index'),
]
