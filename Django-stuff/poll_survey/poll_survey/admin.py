from .models import *
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
	fields = ('email_addr', 'username')

	list_display = ['email_addr', 'username', 'firstname']
	search_fields = ['username']
	list_filter = ['firstname']

admin.site.register(UserProfile, UserProfileAdmin)