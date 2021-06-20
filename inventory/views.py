from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add(request,book_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def delete(request,book_id):
    return HttpResponse("Hello, world. You're at the polls index.")


def view(request,book_id):
    return HttpResponse("Hello, world. You're at the polls index.")