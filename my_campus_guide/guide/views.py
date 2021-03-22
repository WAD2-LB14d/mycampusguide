from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from guide.forms import LecturerForm, UserForm, UserProfileForm

# Create your views here.

def index(request):
  return render(request, 'guide/index.html')

def courses(request):
	return render(request, 'guide/courses.html')

def lecturers(request):
	return render(request, 'guide/lecturers.html')

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
                login(request, user)
                return redirect(reverse('rango:index'))
            else:             
                return HttpResponse("Your Rango account is disabled.")

        else:          
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
            
    else:
        return render(request, 'guide/login.html')