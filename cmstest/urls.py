from django.conf.urls import patterns, url
from cmstest import views

urlpatterns = patterns('',
	# ex: /polls/
	#url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^$', views.testView),
	)