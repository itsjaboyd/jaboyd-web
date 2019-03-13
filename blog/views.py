from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from time import strftime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment

# Create your views here.
def index(request):
	context = {
		'now': strftime("%m/%d/%Y"),
	}
	return render(request, 'blog/index.html', context)

def aboutMe(request):
	context = {
		'now': strftime("%m/%d/%Y"),
	}
	return render(request, 'blog/about-me.html', context)

def journal(request):
	context = {
		'now': strftime("%m/%d/%Y"),
	}
	return render(request, 'blog/journal.html', context)

def resume(request):
	context = {
		'now': strftime("%m/%d/%Y"),
	}
	return render(request, 'blog/resume.html', context)

def contact(request):
	context = {
		'now': strftime("%m/%d/%Y"),
	}
	return render(request, 'blog/contact.html', context)
