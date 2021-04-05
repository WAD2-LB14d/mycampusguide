import os
import re
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
import guide.models
from guide import forms

from django.contrib.auth.models import User
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}MGG TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

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


class MyCampusGuideTemplateTests(TestCase):
	def setUp(self):
		self.project_base_dir = os.getcwd()
		self.templates_dir = os.path.join(self.project_base_dir, 'templates')
		self.guide_templates_dir = os.path.join(self.templates_dir, 'guide')

	def test_templates_directory_exists(self):
		directory_exists = os.path.isdir(self.templates_dir)
		self.assertTrue(directory_exists, f"{FAILURE_HEADER}Template directory does not exist.{FAILURE_FOOTER}")


class MyCampusGuideUsersTests(TestCase):
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




