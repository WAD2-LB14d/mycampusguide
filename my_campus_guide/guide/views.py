from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from guide.forms import LecturerForm

# Create your views here.

def index(request):
  return render(request, 'guide/index.html')

def courses(request):
	return render(request, 'guide/courses.html')

def lecturers(request):
	return render(request, 'guide/lecturers.html')