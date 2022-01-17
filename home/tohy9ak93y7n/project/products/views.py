from django.shortcuts import render


# Create your views here.

def index(request):
    html_file = 'products/index.html'
    return render(request, html_file)
