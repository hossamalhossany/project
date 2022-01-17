from django.shortcuts import render
from .models import Product


# Create your views here.

def index(request):
    html_file = 'products/index.html'
    return render(request, html_file)


def products(request):
    data ={'data': Product.objects.all()}
    html_file = 'products/products.html'
    return render(request, html_file, data)


def product(request):
    html_file = 'products/product.html'
    return render(request, html_file)
