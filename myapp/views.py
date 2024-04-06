from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project, Task

# Create your views here.

def index(request):
  return HttpResponse("Index Page")

def hello(request, username):
  return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
  return HttpResponse("<h1>About Page</h1>")

def projects(request):
  projects = list(Project.objects.values())
  return JsonResponse(projects, safe=False)

def tasks(request, id):
  # task = Task.objects.get(id=id) # Asi sería sin una buena vista del 404
  task = get_object_or_404(Task, id=id)
  return HttpResponse("task: %s" %task.title)