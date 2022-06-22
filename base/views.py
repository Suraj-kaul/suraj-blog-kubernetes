from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'base/home.html')

def project(request):
	return render(request, 'base/project.html')