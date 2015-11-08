from .models import *
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
	fields = ('email_addr', 'username')

	list_display = ['email_addr', 'username', 'firstname']
	search_fields = ['username']
	list_filter = ['firstname']

admin.site.register(UserProfile, UserProfileAdmin)

class PostAdmin(admin.ModelAdmin):
	fields = ('poll_post', 'posted_date', 'posted_by',\
		'slug_post')
	#list_display = ['']
	list_filter = ['posted_date']
	populated_fields = {'slug': ('poll_post',)}

admin.site.register(Poll_Post, PostAdmin)