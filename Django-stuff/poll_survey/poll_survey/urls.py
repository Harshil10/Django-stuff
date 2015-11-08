from django.conf.urls import patterns, include, url
from django.contrib import admin
from poll_survey.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poll_survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', poll_views.list_polls_comments, name='Landing view'),
    url(r'^register/$', login_register_views.user_register, name='Register process'),
    url(r'^login/$', login_register_views.user_login, name='Login view'),
    url(r'^logout_user/$', login_register_views.logout_user, name='Logout View'),
    url(r'^user/posts/$', poll_views.get_posts_auth_user, name='Get Posts'),
    url(r'^posts/(?P<slug>[-\w]+)/$', poll_views.get_details_polls, name='Get Details'),
    url(r'^posts/(?P<slug>[-\w]+)/comment/$', poll_views.comment_post, name='Comment Post'),

)
