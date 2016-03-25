from django.shortcuts import render 
from django.http import HttpResponseRedirect, HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.http import StreamingHttpResponse
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home(request):
	context = {}

	template = "home.html"
	return render(request,template,context)

def gallery(request):
	context = {}

	template = "images.html"
	return render(request,template,context)


def contact(request):
	context = {}

	template = "contact.html"
	return render(request,template,context)


