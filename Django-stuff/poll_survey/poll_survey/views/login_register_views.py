from django.template import RequestContext
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
import json
from django.contrib.sessions.backends.signed_cookies import SessionStore 
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

''' Custom authentication method, using custom model '''

def authenticate(email_addr, password):
	from poll_survey.models import UserProfile
	try:
		user = UserProfile.objects.get(email_addr=email_addr)		
	except UserProfile.DoesNotExist:
		return None
	if user.is_active:
		if user.check_password(password):
			return user
		else:
			return None
	else:
		return None

def get_user(user_id):
	try:
		UserProfile.objects.get(pk=user_id)
	except UserProfile.DoesNotExist:
		return None

#@ensure_csrf_cookie
def landing(request):
	return render(request, 'partials/header.html')

''' user login view, based on valid email and password.
kept csrf decorator for double sure '''

@csrf_protect
def user_login(request):
	print 'i am called'
	if request.method == 'GET':
		if request.user.is_authenticated():
			return redirect(settings.LOGIN_REDIRECT_URL)
		return render(request, 'login.html')
	elif request.method == 'POST':
		try:
			email_addr = request.POST.get('email')
			password = request.POST.get('password')
			next = request.POST.get('next')
			print next
			print request.POST
			user = authenticate(email_addr, password)
			if user != None:
				user.backend = 'django.contrib.auth.backends.ModelBackend'
				try:
					login(request, user)
				except Exception as ex:
					print ex
				if next != '':
					print 'next is there'
					return redirect(next)
				return redirect(settings.LOGIN_REDIRECT_URL)
			else:
				return render(request, 'login.html')

		except Exception as ex:
			print ex
			return None

''' method to retrun message to be shown in template '''

def return_message(request, flag=False):
	if flag:
		messages.success(request, 'Registered ! Thanks very much.')
		return
	messages.error(request, 'Oops !, This email is already registered !')

''' register new user, validation is there to check proper email, double sures 
with client JS 
'''

@csrf_protect
def user_register(request):
	if request.method == 'GET':
		return render(request, 'register.html')
	elif request.method == 'POST':
		try:
			email_addr = request.POST.get('email')
			firstname = request.POST.get('firstname')
			lastname = request.POST.get('lastname')
			username = request.POST.get('username')
			password = request.POST.get('password')
			#print email_addr, firstname, username, password
		except AttributeError:
			return render(request, 'register.html')
		AUTH_MODEL = get_user_model()
		user = AUTH_MODEL.objects.create_user(email_addr, username, firstname=firstname,\
			lastname=lastname, password=password)

		if isinstance(user, tuple):
			error_message = user[1]
			messages.error(request, error_message)
			return redirect('/register/')

		elif user != None:
			return_message(request, flag=True)
			return redirect('/login/')

		return_message(request)
		return render(request, 'register.html')

def logout_user(request):
	logout(request)
	return redirect(settings.LOGIN_URL)
