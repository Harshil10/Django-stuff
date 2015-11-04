from django.conf.urls import patterns, include, url
from django.contrib import admin
from poll_survey.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poll_survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_register_views.landing, name='Landing view'),
    url(r'^register/$', login_register_views.register_user_new, name='Register view'),
    url(r'^register_user/$', login_register_views.register_user, name='Register process'),
    url(r'^login/$', login_register_views.login_form, name='Login view'),
    url(r'^login_process/$', login_register_views.login_process, name='Login process')
)
