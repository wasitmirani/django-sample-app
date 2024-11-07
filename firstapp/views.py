
from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to Django app")

def home(request):
    return HttpResponse("This Django App")