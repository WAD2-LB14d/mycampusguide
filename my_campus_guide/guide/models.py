from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Course(models.Model):
	NAME_MAX_LENGTH = 128
	name = models.CharField(max_length = NAME_MAX_LENGTH, unique = True)
	views = models.IntegerField(default = 0)
	slug = models.SlugField(unique = True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Course, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Courses"

	def __str__(self):
		return self.name


class Lecturer(models.Model):
	NAME_MAX_LENGTH = 128
	name = models.CharField(max_length = NAME_MAX_LENGTH, unique = True)
	views = models.IntegerField(default = 0)
	slug = models.SlugField(unique = True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Lecturer, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Lecturers"

	def __str__(self):
		return self.name
   

class courseComment(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Course, on_delete=models.CASCADE)
   

class lecturerComment(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Lecturer, on_delete=models.CASCADE) 


class courseRating(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Course, on_delete=models.CASCADE)   


class lecturerRating(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Lecturer, on_delete=models.CASCADE)  
