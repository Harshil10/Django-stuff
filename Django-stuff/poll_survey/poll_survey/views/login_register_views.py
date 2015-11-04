from django.template import RequestContext
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model
import json



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

def register_user_new(request):
	if request.method == 'GET':
		print 'inside'
		return render(request, 'register.html')

def login_form(request):
	if request.method == 'GET':
		print request.session.get_expiry_age()
		return render(request, 'login.html')

@csrf_protect
def login_process(request):
	print 'in login process'
	if request.method == 'POST':
		print 'inside post'
		try:
			email_addr = request.POST.get('email')
			password = request.POST.get('password')
			print email_addr, password
			user = authenticate(email_addr, password)
			if user != None:
				user.backend = 'django.contrib.auth.backends.ModelBackend'
				try:
					login(request, user)
				except Exception as ex:
					print ex
				return render(request, 'register.html')
			else:
				return render(request, 'login.html')


		except Exception as ex:
			return None

def return_message(request, flag=False):
	if flag:
		messages.success(request, 'Registered ! Thanks very much.')
		return
	messages.error(request, 'Oops !, This email is already registered !')

@csrf_protect
def register_user(request):
	if request.method == 'POST':
		try:
			email_addr = request.POST.get('email')
			firstname = request.POST.get('firstname', '')
			lastname = request.POST.get('lastname', '')
			username = request.POST.get('username')
			password = request.POST.get('password')
			#print email_addr, firstname, username, password
		except AttributeError:
			return render(request, 'register.html')
		AUTH_MODEL = get_user_model()
		user = AUTH_MODEL.objects.create_user(email_addr, username, firstname=firstname,\
			lastname=lastname, password=password)
		if user != None:
			return_message(request, flag=True)
			return redirect('/login/')
		print 'reacheddddd'
		return_message(request)
		return render(request, 'register.html')

