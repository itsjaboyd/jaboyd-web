from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('index', views.index, name='index'),
	path('about-me', views.aboutMe, name='about-me'),
	path('journal', views.journal, name='journal'),
	path('resume', views.resume, name='resume'),
	path('contact', views.contact, name='contact'),
]
