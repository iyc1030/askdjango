from django.shortcuts import render
from django.conf.urls import url
from . import views

def post_list(request):
    return render(request, 'blog/post_list.html')
