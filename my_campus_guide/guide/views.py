from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from guide.forms import LecturerForm
from guide.models import Lecturer
# Create your views here.

def index(request):
  return render(request, 'guide/index.html')

def courses(request):
  return render(request, 'guide/courses.html')

def lecturers(request):
  lecturers = Lecturer.objects.order_by('name')
  context_dict = {}
  context_dict['lecturers'] = lecturers
  return render(request, 'guide/lecturers.html', context=context_dict)
