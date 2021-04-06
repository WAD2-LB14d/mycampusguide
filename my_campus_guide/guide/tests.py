import os
import re
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
from guide.models import *
from guide import forms

from django.contrib.auth.models import User
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}MGG TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class ProjectStructureTests(TestCase):
	def setUp(self):
		self.project_base_dir = os.getcwd()
		self.templates_dir = os.path.join(self.project_base_dir, 'templates')
		self.guide_templates_dir = os.path.join(self.templates_dir, 'guide')
		self.guide_dir = os.path.join(self.project_base_dir, 'guide')
		self.project_dir = os.path.join(self.project_base_dir, 'my_campus_guide')

	def test_directories_exists(self):
		directory_exists = os.path.isdir(self.templates_dir)
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}Template directory does not exist.{FAILURE_FOOTER}")
		directory_exists = os.path.isdir(self.guide_templates_dir)
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}Templates folder does not contain folder guide.{FAILURE_FOOTER}")
		directory_exists = os.path.isdir(self.guide_dir)
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}Project folder my_campus_guide does not exist.{FAILURE_FOOTER}")
		directory_exists = os.path.isdir(self.project_dir)
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}Application folder guide does not exist.{FAILURE_FOOTER}")

	def test_app_files_exist(self):
		directory_exists = os.path.isfile(os.path.join(self.guide_dir, 'forms.py'))		
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}forms.py file does not exist.{FAILURE_FOOTER}")
		directory_exists = os.path.isfile(os.path.join(self.guide_dir, 'models.py'))		
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}models.py file does not exist.{FAILURE_FOOTER}")
		directory_exists = os.path.isfile(os.path.join(self.guide_dir, 'urls.py'))		
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}urls.py file does not exist.{FAILURE_FOOTER}")
		directory_exists = os.path.isfile(os.path.join(self.guide_dir, 'views.py'))		
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}views.py file does not exist.{FAILURE_FOOTER}")

	def test_templates_files_exist(self):
		directory_exists = os.path.isfile(os.path.join(self.guide_templates_dir, 'index.html'))		
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}index.html page does not exist.{FAILURE_FOOTER}")
		directory_exists = os.path.isfile(os.path.join(self.guide_templates_dir, 'base.html'))		
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}base.html page does not exist.{FAILURE_FOOTER}")
		directory_exists = os.path.isfile(os.path.join(self.guide_templates_dir, 'login.html'))		
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}login.html page does not exist.{FAILURE_FOOTER}")
		directory_exists = os.path.isfile(os.path.join(self.guide_templates_dir, 'index.html'))		
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}index.html page does not exist.{FAILURE_FOOTER}")

	def test_guide_has_urls_module(self):
		module_exists = os.path.isfile(os.path.join(self.project_dir, 'urls.py'))
		self.assertTrue(module_exists, f"{FAILURE_HEADER}The app's urls.py module is missing. You need two urls.py modules.{FAILURE_FOOTER}")
		

class IndexViewsTests(TestCase):
	def setUp(self):
		self.views_module = importlib.import_module('guide.views')
		self.views_module_listing = dir(self.views_module) 
		self.project_urls_module = importlib.import_module('my_campus_guide.urls')
		self.response = self.client.get(reverse('guide:index'))

	def test_index_view_exists(self):
		name_exists = 'index' in self.views_module_listing
		is_callable = callable(self.views_module.index)
        
		self.assertTrue(name_exists, f"{FAILURE_HEADER}The index() view does not exist.{FAILURE_FOOTER}")
		self.assertTrue(is_callable, f"{FAILURE_HEADER}The index view cannot be called.{FAILURE_FOOTER}")

	def test_mappings_exists(self):
		index_mapping_exists = False

		for mapping in self.project_urls_module.urlpatterns:
			if hasattr(mapping, 'name'):
				if mapping.name == 'index':
					index_mapping_exists = True
        
		self.assertTrue(index_mapping_exists, f"{FAILURE_HEADER}The index URL mapping could not be found.{FAILURE_FOOTER}")
		self.assertEquals(reverse('guide:index'), '/guide/', f"{FAILURE_HEADER}The index URL lookup failed.{FAILURE_FOOTER}")

	def test_response(self):
		self.assertEqual(self.response.status_code, 200, f"{FAILURE_HEADER}Requesting the index page failed.{FAILURE_FOOTER}")
		self.assertContains(self.response, 'lecturer', msg_prefix=f"{FAILURE_HEADER}The index view does not return the expected response.{FAILURE_FOOTER}")
		self.assertContains(self.response, 'course', msg_prefix=f"{FAILURE_HEADER}The index view does not return the expected response.{FAILURE_FOOTER}")

	def test_index_uses_template(self):
		self.assertTemplateUsed(self.response, 'guide/index.html', f"{FAILURE_HEADER}Your index() view does not use the expected index.html template.{FAILURE_FOOTER}")
    
	def test_index_starts_with_doctype(self):
		self.assertTrue(self.response.content.decode().startswith('<!DOCTYPE html>'), f"{FAILURE_HEADER}index.html template does not start with <!DOCTYPE html>.{FAILURE_FOOTER}")


class LecturersViewsTests(TestCase):
	def setUp(self):
		self.lecturers_module = importlib.import_module('guide.views')
		self.lecturers_module_listing = dir(self.lecturers_module) 
		self.project_urls_module = importlib.import_module('my_campus_guide.urls')
		self.response = self.client.get(reverse('guide:lecturers'))

	def test_index_view_exists(self):
		name_exists = 'lecturers' in self.lecturers_module_listing
		is_callable = callable(self.lecturers_module.lecturers)
        
		self.assertTrue(name_exists, f"{FAILURE_HEADER}The lecturers() view does not exist.{FAILURE_FOOTER}")
		self.assertTrue(is_callable, f"{FAILURE_HEADER}The lecturers view cannot be called.{FAILURE_FOOTER}")

	def test_mappings_exists(self):
		self.assertEquals(reverse('guide:lecturers'), '/guide/lecturers/', f"{FAILURE_HEADER}The lecturers URL lookup failed.{FAILURE_FOOTER}")

	def test_response(self):
		self.assertEqual(self.response.status_code, 200, f"{FAILURE_HEADER}Requesting the lecturers page failed.{FAILURE_FOOTER}")
		self.assertContains(self.response, 'lecturers', msg_prefix=f"{FAILURE_HEADER}The lecturers view does not return the expected response.{FAILURE_FOOTER}")

	def test_index_uses_template(self):
		self.assertTemplateUsed(self.response, 'guide/lecturers.html', f"{FAILURE_HEADER}Your lecturers() view does not use the expected lecturers.html template.{FAILURE_FOOTER}")
    
	def test_index_starts_with_doctype(self):
		self.assertTrue(self.response.content.decode().startswith('<!DOCTYPE html>'), f"{FAILURE_HEADER}lecturers.html template does not start with <!DOCTYPE html>.{FAILURE_FOOTER}")


class CoursesViewsTests(TestCase):
	def setUp(self):
		self.courses_module = importlib.import_module('guide.views')
		self.courses_module_listing = dir(self.courses_module) 
		self.project_urls_module = importlib.import_module('my_campus_guide.urls')
		self.response = self.client.get(reverse('guide:courses'))

	def test_index_view_exists(self):
		name_exists = 'courses' in self.courses_module_listing
		is_callable = callable(self.courses_module.lecturers)
        
		self.assertTrue(name_exists, f"{FAILURE_HEADER}The courses() view does not exist.{FAILURE_FOOTER}")
		self.assertTrue(is_callable, f"{FAILURE_HEADER}The courses view cannot be called.{FAILURE_FOOTER}")

	def test_mappings_exists(self):
		self.assertEquals(reverse('guide:courses'), '/guide/courses/', f"{FAILURE_HEADER}The courses URL lookup failed.{FAILURE_FOOTER}")

	def test_response(self):
		self.assertEqual(self.response.status_code, 200, f"{FAILURE_HEADER}Requesting the courses page failed.{FAILURE_FOOTER}")
		self.assertContains(self.response, 'courses', msg_prefix=f"{FAILURE_HEADER}The courses view does not return the expected response.{FAILURE_FOOTER}")

	def test_index_uses_template(self):
		self.assertTemplateUsed(self.response, 'guide/courses.html', f"{FAILURE_HEADER}Your courses() view does not use the expected courses.html template.{FAILURE_FOOTER}")
    
	def test_index_starts_with_doctype(self):
		self.assertTrue(self.response.content.decode().startswith('<!DOCTYPE html>'), f"{FAILURE_HEADER}courses.html template does not start with <!DOCTYPE html>.{FAILURE_FOOTER}")


class RegisterViewsTests(TestCase):
	def setUp(self):
		self.register_module = importlib.import_module('guide.views')
		self.register_module_listing = dir(self.register_module) 
		self.project_urls_module = importlib.import_module('my_campus_guide.urls')
		self.response = self.client.get(reverse('guide:register'))

	def test_index_view_exists(self):
		name_exists = 'register' in self.register_module_listing
		is_callable = callable(self.register_module.register)
        
		self.assertTrue(name_exists, f"{FAILURE_HEADER}The register() view does not exist.{FAILURE_FOOTER}")
		self.assertTrue(is_callable, f"{FAILURE_HEADER}The register view cannot be called.{FAILURE_FOOTER}")

	def test_mappings_exists(self):
		self.assertEquals(reverse('guide:register'), '/guide/register/', f"{FAILURE_HEADER}The register URL lookup failed.{FAILURE_FOOTER}")

	def test_response(self):
		self.assertEqual(self.response.status_code, 200, f"{FAILURE_HEADER}Requesting the register page failed.{FAILURE_FOOTER}")
		self.assertContains(self.response, 'register', msg_prefix=f"{FAILURE_HEADER}The register view does not return the expected response.{FAILURE_FOOTER}")
		self.assertContains(self.response, 'user', msg_prefix=f"{FAILURE_HEADER}The register view does not return the expected response.{FAILURE_FOOTER}")

	def test_index_uses_template(self):
		self.assertTemplateUsed(self.response, 'guide/register.html', f"{FAILURE_HEADER}Your register() view does not use the expected register.html template.{FAILURE_FOOTER}")
    
	def test_index_starts_with_doctype(self):
		self.assertTrue(self.response.content.decode().startswith('<!DOCTYPE html>'), f"{FAILURE_HEADER}register.html template does not start with <!DOCTYPE html>.{FAILURE_FOOTER}")



class MyCampusGuideUsersTests(TestCase):
	def create_user_object():
		user = User.objects.get_or_create(username='testuser',
		                                      first_name='Test',
		                                      last_name='User',
		                                      email='test@test.com')[0]
		user.set_password('testabc123')
		user.save()

		return user

	def create_super_user_object():
		return User.objects.create_superuser('admin', 'admin@test.com', 'testpassword')


	def test_user_form(self):
		
		user_form = forms.UserForm()
		self.assertEqual(type(user_form.__dict__['instance']), User, f"{FAILURE_HEADER}UserForm does not match up to the User model{FAILURE_FOOTER}")

		fields = user_form.fields
		
		expected_fields = {
			'username': django_fields.CharField,
			'email': django_fields.EmailField,
			'password': django_fields.CharField,
		}
        
		for expected_field_name in expected_fields:
			expected_field = expected_fields[expected_field_name]

			self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field {expected_field_name} was not found in the UserForm form. Check you have complied with the specification, and try again.{FAILURE_FOOTER}")
			self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field {expected_field_name} in UserForm was not of the correct type. Expected {expected_field}; got {type(fields[expected_field_name])}.{FAILURE_FOOTER}")


class MyCampusGuideModelsTests(TestCase):
	def setUp(self):  
		user = User.objects.get_or_create(username='testuser',
		                                      first_name='Test',
		                                      last_name='User',
		                                      email='test@test.com')[0]

		lc = Category.objects.get_or_create(name="Lecturer Pages", views=4)[0]
		cc = Category.objects.get_or_create(name="Course Pages", views=2)[0]

		Lecturer.objects.get_or_create(name='Test Lecturer',
										teaching= 'Computing',
										description= 'This is the test lecturer.', 
										views= 5,
										category = Category.objects.get(name="Lecturer Pages"))

		Course.objects.get_or_create(name= 'Test Course',
									school= 'Science and Engineering',
									credits= 20, 
									year= 2021, 
									requirements='None.',
									currentlecturer= 'Test Lecturer',
									description= 'You will be tested.',
									views= 2,
									category = Category.objects.get(name="Course Pages"))

		CourseComment.objects.get_or_create(date = datetime.datetime(2020, 5, 17),
											comment = "I love it",
											user = User.objects.get(username='testuser'),
											page = Course.objects.get(name='Test Course'))

		LecturerComment.objects.get_or_create(date = datetime.datetime(2021, 1, 14),
											comment = "I hate it",
											user = User.objects.get(username='testuser'),
											page = Lecturer.objects.get(name='Test Lecturer'))

		LecturerRating.objects.get_or_create(date = datetime.datetime(2020, 6, 8),
											rating = 3,
											user = User.objects.get(username='testuser'),
											page = Lecturer.objects.get(name='Test Lecturer'))

		CourseRating.objects.get_or_create(date = datetime.datetime(2021, 2, 4),
											rating = 4,
											user = User.objects.get(username='testuser'),
											page = Course.objects.get(name='Test Course'))

	def test_category_model(self):
		category_py = Category.objects.get(name='Lecturer Pages')
		self.assertEqual(category_py.views, 4, f"{FAILURE_HEADER}Tests on the Category model failed.{FAILURE_FOOTER}")
        
	def test_lecturer_model(self):
		lecturer = Lecturer.objects.get(name='Test Lecturer')
		self.assertEqual(lecturer.teaching, 'Computing', f"{FAILURE_HEADER}Tests on the lecturer model failed.{FAILURE_FOOTER}")
		self.assertEqual(lecturer.views, 5, f"{FAILURE_HEADER}Tests on the lecturer model failed.{FAILURE_FOOTER}")
		self.assertEqual(lecturer.description, 'This is the test lecturer.', f"{FAILURE_HEADER}Tests on the lecturer model failed.{FAILURE_FOOTER}")
		self.assertEqual(lecturer.category, Category.objects.get(name="Lecturer Pages"), f"{FAILURE_HEADER}Tests on the lecturer model failed.{FAILURE_FOOTER}")

	def test_course_model(self):
		course = Course.objects.get(name='Test Course')
		self.assertEqual(course.school, 'Science and Engineering', f"{FAILURE_HEADER}Tests on the course model failed.{FAILURE_FOOTER}")
		self.assertEqual(course.credits, 20, f"{FAILURE_HEADER}Tests on the course model failed.{FAILURE_FOOTER}")
		self.assertEqual(course.year, 2021, f"{FAILURE_HEADER}Tests on the lecturer model failed.{FAILURE_FOOTER}")
		self.assertEqual(course.requirements, 'None.', f"{FAILURE_HEADER}Tests on the lecturer model failed.{FAILURE_FOOTER}")
		self.assertEqual(course.currentlecturer, 'Test Lecturer', f"{FAILURE_HEADER}Tests on the lecturer model failed.{FAILURE_FOOTER}")
		self.assertEqual(course.description, 'You will be tested.', f"{FAILURE_HEADER}Tests on the lecturer model failed.{FAILURE_FOOTER}")
		self.assertEqual(course.views, 2, f"{FAILURE_HEADER}Tests on the lecturer model failed.{FAILURE_FOOTER}")
		self.assertEqual(course.category, Category.objects.get(name="Course Pages"), f"{FAILURE_HEADER}Tests on the lecturer model failed.{FAILURE_FOOTER}")

	def test_coursecomment_model(self):
		user = User.objects.get(username = "testuser")
		course = Course.objects.get(name='Test Course')
		comment = CourseComment.objects.get(user = user, page = course)
		self.assertEqual(comment.date.day, 17, f"{FAILURE_HEADER}Tests on the course comments model failed.{FAILURE_FOOTER}")
		self.assertEqual(comment.date.month, 5, f"{FAILURE_HEADER}Tests on the course comments model failed.{FAILURE_FOOTER}")
		self.assertEqual(comment.date.year, 2020, f"{FAILURE_HEADER}Tests on the course comments model failed.{FAILURE_FOOTER}")
		self.assertEqual(comment.comment, 'I love it', f"{FAILURE_HEADER}Tests on the course comments model failed.{FAILURE_FOOTER}")
		self.assertEqual(comment.user, User.objects.get(username='testuser'), f"{FAILURE_HEADER}Tests on the course comments model failed.{FAILURE_FOOTER}")
		self.assertEqual(comment.page, Course.objects.get(name='Test Course'), f"{FAILURE_HEADER}Tests on the course comments model failed.{FAILURE_FOOTER}")

	def test_lecturercomment_model(self):
		user = User.objects.get(username = "testuser")
		lecturer = Lecturer.objects.get(name='Test Lecturer')
		comment = LecturerComment.objects.get(user = user, page = lecturer)
		self.assertEqual(comment.date.day, 14, f"{FAILURE_HEADER}Tests on the lecturer comments model failed.{FAILURE_FOOTER}")
		self.assertEqual(comment.date.month, 1, f"{FAILURE_HEADER}Tests on the lecturer comments model failed.{FAILURE_FOOTER}")
		self.assertEqual(comment.date.year, 2021, f"{FAILURE_HEADER}Tests on the lecturer comments model failed.{FAILURE_FOOTER}")
		self.assertEqual(comment.comment, 'I hate it', f"{FAILURE_HEADER}Tests on the lecturer comments model failed.{FAILURE_FOOTER}")
		self.assertEqual(comment.user, User.objects.get(username='testuser'), f"{FAILURE_HEADER}Tests on the lecturer comments model failed.{FAILURE_FOOTER}")
		self.assertEqual(comment.page, Lecturer.objects.get(name='Test Lecturer'), f"{FAILURE_HEADER}Tests on the lecturer comments model failed.{FAILURE_FOOTER}")

	def test_lecturerrating_model(self):
		user = User.objects.get(username = "testuser")
		lecturer = Lecturer.objects.get(name='Test Lecturer')
		rating = LecturerRating.objects.get(user = user, page = lecturer)
		self.assertEqual(rating.date.day, 8, f"{FAILURE_HEADER}Tests on the lecturer rating model failed.{FAILURE_FOOTER}")
		self.assertEqual(rating.date.month, 6, f"{FAILURE_HEADER}Tests on the lecturer rating model failed.{FAILURE_FOOTER}")
		self.assertEqual(rating.date.year, 2020, f"{FAILURE_HEADER}Tests on the lecturer rating model failed.{FAILURE_FOOTER}")
		self.assertEqual(rating.rating, 3, f"{FAILURE_HEADER}Tests on the lecturer rating model failed.{FAILURE_FOOTER}")
		self.assertEqual(rating.user, User.objects.get(username='testuser'), f"{FAILURE_HEADER}Tests on the lecturer rating model failed.{FAILURE_FOOTER}")
		self.assertEqual(rating.page, Lecturer.objects.get(name='Test Lecturer'), f"{FAILURE_HEADER}Tests on the lecturer rating model failed.{FAILURE_FOOTER}")

	def test_courserating_model(self):
		user = User.objects.get(username = "testuser")
		course = Course.objects.get(name='Test Course')
		rating = CourseRating.objects.get(user = user, page = course)
		self.assertEqual(rating.date.day, 4, f"{FAILURE_HEADER}Tests on the course rating model failed.{FAILURE_FOOTER}")
		self.assertEqual(rating.date.month, 2, f"{FAILURE_HEADER}Tests on the course rating model failed.{FAILURE_FOOTER}")
		self.assertEqual(rating.date.year, 2021, f"{FAILURE_HEADER}Tests on the course rating model failed.{FAILURE_FOOTER}")
		self.assertEqual(rating.rating, 4, f"{FAILURE_HEADER}Tests on the course rating model failed.{FAILURE_FOOTER}")
		self.assertEqual(rating.user, User.objects.get(username='testuser'), f"{FAILURE_HEADER}Tests on the course rating model failed.{FAILURE_FOOTER}")
		self.assertEqual(rating.page, Course.objects.get(name='Test Course'), f"{FAILURE_HEADER}Tests on the course rating model failed.{FAILURE_FOOTER}")


class test_population_script(TestCase):
	def setUp(self):
		try:
			import population_script
		except ImportError:
			raise ImportError(f"{FAILURE_HEADER}Could not import the population script. Check it's in the right location.{FAILURE_FOOTER}")	        
		if 'populate' not in dir(population_script):
			raise NameError(f"{FAILURE_HEADER}The populate() function does not exist.{FAILURE_FOOTER}")	        
		population_script.populate()	

	def test_lecturer_pages(self):
		lecturers = Lecturer.objects.filter()
		lecturers_len = len(lecturers)
		lecturers_strs = map(str, lecturers)
        
		self.assertEqual(lecturers_len, 8, f"{FAILURE_HEADER}Expecting 8 lecturers pages in the population script; found {lecturers_len}.{FAILURE_FOOTER}")
		self.assertTrue('Gethin Norman' in lecturers_strs, f"{FAILURE_HEADER}The page 'Gethin Norman' was expected but not created.{FAILURE_FOOTER}")

	def test_course_pages(self):
		course = Course.objects.filter()
		course_len = len(course)
		course_strs = map(str, course)
        
		self.assertEqual(course_len, 7, f"{FAILURE_HEADER}Expecting 7 course pages in the population script; found {course_len}.{FAILURE_FOOTER}")
		self.assertTrue('Web App Development 2' in course_strs, f"{FAILURE_HEADER}The page 'Web App Development 2' was expected but not created.{FAILURE_FOOTER}")

