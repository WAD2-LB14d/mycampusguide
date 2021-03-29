from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from guide.models import Lecturer, Course
from guide.forms import LecturerForm, CourseForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
  return render(request, 'guide/index.html')

def profile(request):
  return render(request, 'guide/profile.html')

def courses(request):
  courses = Course.objects.order_by('name')
  for course in courses:
    course.storeNumberOfComments()
  context_dict = {}
  context_dict['courses'] = courses
  return render(request, 'guide/courses.html', context=context_dict)

def lecturers(request):
  lecturers = Lecturer.objects.order_by('name')
  for lecturer in lecturers:
    lecturer.storeNumberOfComments()
  context_dict = {}
  context_dict['lecturers'] = lecturers
  return render(request, 'guide/lecturers.html', context=context_dict)

def add_course(request):
  form = CourseForm()
  if request.method == 'POST':
      form = CourseForm(request.POST)

      if form.is_valid():
        page.category = category
        page.save()

        return redirect(reverse('guide:courses'))
      else:
        print(form.errors)
  return render(request, 'guide/add_course.html', {'form':form})

def add_lecturer(request):
  form = LecturerForm()
  if request.method == 'POST':
      form = LecturerForm(request.POST)

      if form.is_valid():
        page.category = category
        page.save()

        return redirect(reverse('guide:lecturers'))
      else:
        print(form.errors)
  return render(request, 'guide/add_lecturer.html', {'form':form})


def show_lecturer(request, lecturer_name_slug):
  context_dict = {}
  try:
    lecturer = Lecturer.objects.get(slug=lecturer_name_slug)
    context_dict['lecturer'] = lecturer
  except Lecturer.DoesNotExist:
    context_dict['lecturer'] = None
  return render(request, 'guide/chosen_lecturer.html', context = context_dict)


def show_course(request, course_name_slug):
  context_dict = {}
  try:
    course = Course.objects.get(slug=course_name_slug)
    context_dict['course'] = course
  except Lecturer.DoesNotExist:
    context_dict['course'] = None
  return render(request, 'guide/chosen_course.html', context = context_dict)



def register(request):
  registered = False

  if request.method == 'POST':
    user_form = UserForm(request.POST)
    profile_form = UserProfileForm(request.POST)

    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()

      profile = profile_form.save(commit=False)
      profile.user = user

      if 'picture' in request.FILES:
        profile.picture = request.FILES['picture']

      profile.save()

      registered = True
    else:
      print(user_form.errors, profile_form.errors)
  else:
    user_form = UserForm()
    profile_form = UserProfileForm()

        
  return render(request, 'guide/register.html',context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})  

def login(request):
    
    if request.method == 'POST':       
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:          

            if user.is_active:                
                auth_login(request, user)
                return redirect(reverse('guide:index'))
            else:             
                return HttpResponse("Your Guide account is disabled.")

        else:          
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
            
    else:
        return render(request, 'guide/login.html')

@login_required
def logout(request):
  auth_logout(request)
  return render(request, 'guide/logout.html')