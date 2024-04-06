from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("Index Page")

def hello(request, username):
  return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
  return HttpResponse("<h1>About Page</h1>")