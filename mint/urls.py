from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('',
	url(r'^home/$', 'budget.views.home', name='home'),
	url(r'^upload/$', 'budget.views.upload_file', name='upload_file'),
)
