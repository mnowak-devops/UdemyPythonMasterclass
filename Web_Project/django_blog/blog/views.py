from django.shortcuts import render
from django.http import response, HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Welcome to my blog")
