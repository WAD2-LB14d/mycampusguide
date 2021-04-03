from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from guide.models import Lecturer, Course, UserProfile, LecturerRating, Category, CourseRating
from guide.forms import LecturerForm, CourseForm, UserForm, UserProfileForm, LecturerRatingForm, CourseRatingForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def visitor_cookie_handler(request, response): 
  visits = int(request.COOKIES.get('visits', '1'))
  last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now())) 
  last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
  if (datetime.now() - last_visit_time).days > 0:
    visits = visits + 1
  else:
    response.set_cookie('visits', visits)


def index(request):
  response =  render(request, 'guide/index.html')
  visitor_cookie_handler(request, response)
  return response


@login_required
def myprofile(request):
    user = User.objects.get(username=request.user.username)
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'guide/myprofile.html', context={'user': user, 'profile': profile})

def courses(request):
  courses = Course.objects.order_by('name')
  for course in courses:
    course.storeNumberOfComments()
    course.calculateAverageRating()
    course.save()
  order_by = request.GET.get('order_by', 'name')
  courses = Course.objects.order_by(order_by)  
  context_dict = {}
  context_dict['courses'] = courses
  return render(request, 'guide/courses.html', context=context_dict)

def lecturers(request):
  lecturers = Lecturer.objects.order_by('name')
  for lecturer in lecturers:
    lecturer.storeNumberOfComments()
    lecturer.calculateAverageRating()
    lecturer.save()
  order_by = request.GET.get('order_by', 'name')
  lecturers = Lecturer.objects.order_by(order_by)  
  context_dict = {}
  context_dict['lecturers'] = lecturers
  return render(request, 'guide/lecturers.html', context=context_dict)

@login_required
def add_course(request):
  category = Category.objects.get(name="Course Pages")

  form = CourseForm()
  if request.method == 'POST':
      form = CourseForm(request.POST)

      if form.is_valid():
        page = form.save(commit=False)
        page.category = category
        page.views = 0
        page.save()

        return redirect(reverse('guide:courses'))
      else:
        print(form.errors)
  return render(request, 'guide/add_course.html', {'form':form})

@login_required
def add_lecturer(request):
  category = Category.objects.get(name="Lecturer Pages")

  form = LecturerForm()
  if request.method == 'POST':
      form = LecturerForm(request.POST)

      if form.is_valid():
        page = form.save(commit=False)
        page.category = category
        page.views = 0
        page.save()

        return redirect(reverse('guide:lecturers'))
      else:
        print(form.errors)
  return render(request, 'guide/add_lecturer.html', {'form':form})


def show_lecturer(request, lecturer_name_slug):
  context_dict = {}
  try:
    lecturer = Lecturer.objects.get(slug=lecturer_name_slug)
    lecturer.calculateAverageRating()
    context_dict['lecturer'] = lecturer
    context_dict['comments'] = lecturer.lecturercomment_set.all()
    
    try:
      user = User.objects.get(username=request.user.username) 
      context_dict['rating'] = LecturerRating.objects.get(user=user, page=lecturer)
    except:
      context_dict['rating'] = None

  except Lecturer.DoesNotExist:
    context_dict['lecturer'] = None
    context_dict['rating'] = None

  form = LecturerRatingForm()
  if request.method == 'POST':
      form = LecturerRatingForm(request.POST)

      if form.is_valid():
        rating = form.save(commit=False)
        rating.user = request.user
        rating.page = lecturer
        rating.save()

        return render(request, 'guide/chosen_lecturer.html', context = context_dict)
  
  context_dict['form'] = form
  return render(request, 'guide/chosen_lecturer.html', context = context_dict)


def show_course(request, course_name_slug):
  context_dict = {}
  try:
    course = Course.objects.get(slug=course_name_slug)
    course.calculateAverageRating()
    context_dict['course'] = course

    try:
      user = User.objects.get(username=request.user.username)  
      context_dict['rating'] = CourseRating.objects.get(user=user, page=course)
    except:
      context_dict['rating'] = None

  except Course.DoesNotExist:
    context_dict['course'] = None
    context_dict['rating'] = None

  form = CourseRatingForm()
  if request.method == 'POST':
      form = CourseRatingForm(request.POST)

      if form.is_valid():
        rating = form.save(commit=False)
        rating.user = request.user
        rating.page = course
        rating.save()

        return render(request, 'guide/chosen_course.html', context = context_dict)
  
  context_dict['form'] = form
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

      auth_login(request, user)
      return redirect(reverse('guide:index'))
      
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
