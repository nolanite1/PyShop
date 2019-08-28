from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product

def index(request):
    products = Product.objects.all()
    # return HttpResponse('Hello World')
    return render(request,'index.html',{'products':products})

def new(request):
    return HttpResponse('New Products')