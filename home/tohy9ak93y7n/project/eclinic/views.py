from django.shortcuts import render


# Create your views here.

def index(request):
    html_file = 'eclinic/index.html'
    return render(request, html_file)
    return render(request, html_file)


def modules(request):
    html_file = 'eclinic/modules.html'
    return render(request, html_file)
