from django.contrib import admin
from django.urls import path, include
from .views import Home, Article

urlpatterns = [
    path('', Home.as_view()),
    path('articles', Article.as_view())
]
