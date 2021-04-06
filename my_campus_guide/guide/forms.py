from django import forms 
from guide.models import Course, Lecturer, LecturerRating, CourseRating, CourseComment, LecturerComment
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from guide.models import UserProfile
import datetime




class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []  


class CourseForm(forms.ModelForm):
	name = forms.CharField( max_length=128,
						   help_text="Please enter the course name.") 
	school = forms.CharField(max_length=30,
						   help_text="Please enter the course's school.") 
	credits = forms.IntegerField( 
							help_text='Please enter how many credits the course is worth.') 
	requirements = forms.CharField(max_length=100,
						   help_text="Please enter the course requirements.")
	description = forms.CharField(max_length=200,
						   help_text="Please enter a short description of the course.")
	currentlecturer = forms.CharField(max_length=30,
						   help_text="Please enter the current lecturer.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0) 


	class Meta:
		model = Course
		fields = ('name', 'school', 'credits', 'requirements', 'description', 'currentlecturer')




class LecturerForm(forms.ModelForm):
	name = forms.CharField(max_length=50,
						   help_text="Please enter the lecturer's name.") 
	teaching = forms.CharField(max_length=100,
						   help_text="Please enter what the lecturer teaches.") 
	description = forms.CharField(max_length=280,
						   help_text="Please enter a short bio for the lecturer.")
	picture = forms.ImageField(help_text="Please enter an image for the lecturer.",
							required=False)

	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0) 



	class Meta:
		model = Lecturer
		fields = ('name', 'teaching', 'description', 'picture')



class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=30,
						   help_text="Please enter your username.") 
	email = forms.EmailField(max_length=254,
						   help_text="Please enter your Glasgow University email.") 
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


class LecturerRatingForm(forms.ModelForm):
	rating = forms.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)])
	class Meta:
		model = LecturerRating
		fields = ('rating',)


class CourseRatingForm(forms.ModelForm):
	rating = forms.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)])
	class Meta:
		model = CourseRating
		fields = ('rating',)

class LecturerCommentForm(forms.ModelForm):
	comment = forms.CharField(max_length=200)
	class Meta:
		model = LecturerComment
		fields = ('comment',)

class CourseCommentForm(forms.ModelForm):
	comment = forms.CharField(max_length=200)
	class Meta:
		model = CourseComment
		fields = ('comment',)

class ChangeProfileForm(forms.ModelForm):
	email = forms.CharField(max_length=254)
	major = forms.CharField(max_length=30)
	degreeprogram = forms.CharField(max_length=14)
	startedstudying = forms.DateField()
	expectedgraduation = forms.DateField()
	picture = forms.ImageField(required=False)
	class Meta:
		model = UserProfile
		fields = ('email', 'major', 'degreeprogram', 'startedstudying', 'expectedgraduation', 'picture')

class EditLecturer(forms.ModelForm):
	teaching = forms.CharField(max_length=100)
	description = forms.CharField(max_length=280)

	class Meta:
		model = Lecturer
		fields = ('teaching', 'description')

class EditCourse(forms.ModelForm):
	school = forms.CharField(max_length=30)
	credits = forms.IntegerField()
	requirements = forms.CharField(max_length=100)
	description = forms.CharField(max_length=200)
	currentlecturer = forms.CharField(max_length=30)


	class Meta:
		model = Course
		fields = ('school', 'credits', 'requirements', 'description', 'currentlecturer')


