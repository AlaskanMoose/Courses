from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^$', views.index, name='index'),
	url(r'^add_course$', views.add, name='add_course'),
	# url(r'^destroy$', views.destroy)
	url(r'^destroy/(?P<id>\d+)$', views.destroy),
	url(r'^yes$', views.yes),
	url(r'^no$', views.no),
]