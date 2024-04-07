from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Project, Task

# Create your views here.

def index(request):
  title = 'Django Course!!!'
  return render(request, 'index.html', {
    'title': title,
  })

def about(request):
  username = 'Alejandro'
  return render(request, 'about.html', {
    'username': username,
  })

def hello(request, username):
  return HttpResponse("<h1>Hello %s</h1>" %username)

def projects(request):
  # projects = list(Project.objects.values())
  projects = Project.objects.all()
  return render(request, 'projects.html', {
    'projects': projects,
  })

def tasks(request):
  # task = Task.objects.get(id=id) # Asi sería sin una buena vista del 404
  # task = get_object_or_404(Task, id=id)
  return render(request, 'tasks.html')