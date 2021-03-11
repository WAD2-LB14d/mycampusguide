from django import forms 
from rango.models import Course, Lecturer
from django.contrib.auth.models import User
from rango.models import UserProfile


class CourseForm(forms.ModelForm):
	name = forms.CharField(max_length=Course.NAME_MAX_LENGTH,
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
	credits = forms.IntegerField(widget=forms.HiddenInput(), initial=0, 
							help_text='Please enter how many credits the course is worth') 
	bio = forms.CharField(max_length=280,
						   help_text="Please enter a short bio for the lecturer.")
	picture = forms.ImageField()


	#
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0) 



	class Meta:
		model = Course
		fields = ('name', 'teaching', 'bio', 'picture')