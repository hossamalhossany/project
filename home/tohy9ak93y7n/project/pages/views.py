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
    # get data from template
    username_from_temp = request.POST.get('username')
    password_from_temp = request.POST.get('password')

    # join data_from template to table
    data = Login(username=username_from_temp, password=password_from_temp)

    # save the data
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

