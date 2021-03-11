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
    name = models.CharField(max_length = 128, unique = True)
    school = models.CharField(max_length = 30)
    year = models.IntegerField(default=datetime.datetime.now().year)
    requirements = models.CharField(max_length = 100)
    currentlecturer = models.CharField(max_length = 30)
    description = models.CharField(max_length = 200)
    views = models.IntegerField(default = 0)
    pageowner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
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
    name = models.CharField(max_length = 50, unique = True)
    teaching = models.CharField(max_length = 100)
    description = models.CharField(max_length = 280)
    picture = models.ImageField(upload_to='lecturer_images', blank=True)
    views = models.IntegerField(default = 0)
    pageowner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    slug = models.SlugField(unique = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Lecturer, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Lecturers"

    def __str__(self):
        return self.name
   

class UserProfile(models.Model):
    user = models.OnetToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(254)
    username = models.CharField(30)
    major = models.CharField(30)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    degreeprogram = models.CharField(14)
    startedstudying = models.DateField(_("Date"), default=datetime.date.today)
    expectedgraduation = models.DateField(_("Date"), default=datetime.date.today)

    def __str__(self):
        return self.username



class CourseComment(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    page = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "CourseComments"

    def __str__(self):
        return self.comment
   

class LecturerComment(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    page = models.ForeignKey(Lecturer, on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = "LecturerComments"

    def __str__(self):
        return self.comment


class CourseRating(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    page = models.ForeignKey(Course, on_delete=models.CASCADE)   

    class Meta:
        verbose_name_plural = "CourseRatings"

    def __str__(self):
        return self.rating


class LecturerRating(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    page = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "LecturerRatings"

    def __str__(self):
        return self.rating