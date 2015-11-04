from django.conf.urls import patterns, include, url
from django.contrib import admin
from poll_survey.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poll_survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_register_views.landing, name='Landing view'),
    url(r'^register/$', login_register_views.user_register, name='Register process'),
    url(r'^login/$', login_register_views.user_login, name='Login view'),
)
