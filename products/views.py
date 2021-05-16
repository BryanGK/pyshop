from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('This is the /products')


def index_new(request):
    return HttpResponse('This is the /products/new page')

