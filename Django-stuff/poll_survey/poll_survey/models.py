from poll_survey.views import *
from datetime import datetime
from django.db import models
from django.contrib.auth.models import (BaseUserManager,\
	AbstractBaseUser)
from django.db import IntegrityError

''' our custom Manager for our custom user auth model UserProfile '''

class UserProfileManager(BaseUserManager):
	def create_user(self, email_addr, username, firstname=None,\
	 lastname=None, password=None):
		if not email_addr or email_addr == '':
			return (None, 'Empty or invalid Email')
		user = self.model(email_addr=self.normalize_email(email_addr), username=username,\
			firstname=firstname, lastname=lastname)

		user.set_password(password)
		try:
			user.save(using=self._db)
		except IntegrityError:
			return None
		return user

	def create_superuser(self, email_addr, username, firstname=None,\
	 lastname=None, password=None):
		user_admin = self.create_user(email_addr=email_addr, username=username, \
			firstname=firstname, lastname=lastname)
		user_admin.is_admin = True
		user_admin.save(using=self._db)
		return user_admin

''' custom authentication model instead of User '''

class UserProfile(AbstractBaseUser):
	email_addr = models.EmailField(max_length=50, unique=True)
	username = models.TextField(max_length=50, null=True)
	firstname = models.CharField(max_length=50, null=True)
	lastname = models.CharField(max_length=50, null=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	def __str__(self):
		return self.username

	USERNAME_FIELD = 'email_addr'
	REQUIRED_FIELDS = ['username', 'firstname']

	objects = UserProfileManager()

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return self.username

	@property
	def is_staff(self):
		return self.is_admin

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True
