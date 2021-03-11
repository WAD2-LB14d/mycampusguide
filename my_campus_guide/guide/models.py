from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Course(models.Model):
	NAME_MAX_LENGTH = 128
	name = models.CharField(max_length = NAME_MAX_LENGTH, unique = True)
	views = models.IntegerField(default = 0)
	slug = models.SlugField(unique = True)


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


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Lecturer, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Lecturers"

	def __str__(self):
		return self.name