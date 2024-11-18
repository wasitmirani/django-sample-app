
from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("Welcome to Django app")


def home(request):
    # obj = Orders.objects.all()
    template_name = 'home/index.html'
    context = {'obj': []}
    return render(request, template_name, context)
