from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from commonbox.views import *
from commonbox.api import *

common_resource = CommonResource()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^login$', clientlogin),
    url(r'^search$', search),
    url(r'^demo$', demo),                      
    url(r'^search_result$', search_result),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(common_resource.urls)),
)
urlpatterns += staticfiles_urlpatterns()

