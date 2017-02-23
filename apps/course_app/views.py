from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
		"courses": Course.objects.all(),
	}
	return render(request, 'course_app/index.html', context)

def add(request):
	if request.method == 'POST':
		print request.POST
		Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')
def destroy(request, id):
	if request.method == 'POST':
		print request.POST
		context = {
			"courses":Course.objects.filter(id=request.POST['course_id']),
		}
	return render(request, 'course_app/destroy.html', context)

def yes(request):
	if request.method == 'POST':
		print request.POST
		Course.objects.filter(id=request.POST['course_id']).delete()
	return redirect('/')

def no(request):
	return redirect('/')
