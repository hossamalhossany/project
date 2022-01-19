from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .forms import Login_form



# Create your views here.


def index(request):
    data = {"name": "mohamed", "age": 53652363, "address": "giza"}
    html_file = 'pages/index.html'
    return render(request, html_file, data)


def about(request):
    if request.method == 'POST':
        # put (request.POST) which come from template to forms.py (Login_form)
        # forms.py (Login_form) is connected with models
        # this mean data come from template to views.py then go to forms.py then go to models.py
        data = Login_form(request.POST)
        # save the data
        if data.is_valid():
            data.save()

    # create form by forms.py
    data_form = {'login_form': Login_form}

    html_file = 'pages/about.html'
    return render(request, html_file, data_form)


def contact(request):
    return HttpResponse("contact")


def info(request):
    html_file = 'pages/info.html'
    return render(request, html_file)

