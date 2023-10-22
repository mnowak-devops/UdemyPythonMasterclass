from django.shortcuts import render
from django.http import response, HttpResponse
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to my blog")
    def post(self, request):
        return HttpResponse("[POST] Welcome to my blog")

