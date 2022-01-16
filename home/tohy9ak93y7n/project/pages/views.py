from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    data = {"name": "mohamed", "age": 53652363, "address": "giza"}
    html_file = 'pages/index.html'
    return render(request, html_file, data)


def about(request):
    return HttpResponse("ABOUT")


def contact(request):
    return HttpResponse("contact")


def info(request):
    html_file = 'pages/info.html'
    return render(request, html_file)
