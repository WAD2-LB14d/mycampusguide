from django import forms 
from guide.models import Course, Lecturer
from django.contrib.auth.models import User
from guide.models import UserProfile
import datetime


class CourseForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
						   help_text="Please enter the course name.") 
	school = forms.CharField(max_length=30,
						   help_text="Please enter the course's school.") 
	credits = forms.IntegerField(widget=forms.HiddenInput(), initial=0, 
							help_text='Please enter how many credits the course is worth.') 
	requirements = forms.CharField(max_length=100,
						   help_text="Please enter the course requirements.")
	description = forms.CharField(max_length=200,
						   help_text="Please enter a short description of the course.")
	
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0) 


	class Meta:
		model = Course
		fields = ('name', 'school', 'credits', 'requirements', 'description')




class LecturerForm(forms.ModelForm):
	name = forms.CharField(max_length=50,
						   help_text="Please enter the lecturer's name.") 
	teaching = forms.CharField(max_length=100,
						   help_text="Please enter what the lecturer teaches.") 
	description = forms.CharField(max_length=280,
						   help_text="Please enter a short bio for the lecturer.")
	picture = forms.ImageField(help_text="Please enter an image for the lecturer.")

	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0) 



	class Meta:
		model = Course
		fields = ('name', 'teaching', 'description', 'picture')



class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=30,
						   help_text="Please enter your username.") 
	email = forms.CharField(max_length=254,
						   help_text="Please enter your email.") 
	password = forms.CharField(widget=forms.PasswordInput(),
						   help_text ="Please enter your password.")
	major = forms.CharField(max_length=30,
						   help_text="Please enter your major.")
	degreeprogram = forms.CharField(max_length=14,
						   help_text="Please enter your degree program.")
	startedstudying = forms.DateField(initial=datetime.date.today, 
							help_text='Please enter when you started studying.')
	expectedgraduation = forms.DateField(initial=datetime.date.today, 
							help_text='Please enter your expected graduation date.')
	picture = forms.ImageField(help_text="Please enter a picture", required=False)

	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('major', 'picture', 'degreeprogram', 'startedstudying', 'expectedgraduation')
