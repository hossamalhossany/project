from django.shortcuts import render
from .models import Product


# Create your views here.

def index(request):
    html_file = 'products/index.html'
    return render(request, html_file)


def products(request):
    # data = {'data1': Product.objects.get(name='ahmed')}

    # data = {'data1': Product.objects.filter(name='ahmed')}
    all_objects = Product.objects.all()
    data = {'data1': all_objects.filter(price__range=[10, 30])}

    html_file = 'products/products.html'
    return render(request, html_file, data)


def product(request):
    html_file = 'products/product.html'
    return render(request, html_file)
