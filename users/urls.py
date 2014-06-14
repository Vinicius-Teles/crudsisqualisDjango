from django.conf.urls import patterns, url
from users import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^cadastro/$', views.index, name='index'),
	url(r'^busca/$', views.search, name='search'),
	url(r'^delete/(?P<user_id>\d+)/$', views.delete, name='delete'),
	url(r'^update/(?P<user_id>\d+)/$', views.update, name='update'),
)