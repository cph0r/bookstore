import datetime

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render

from .models import *
from .constants import *
import requests


def index(request):
    if request.POST == POST:
        print(POST)
    return render(request, BASE_PATH, {})


def add(request):
    if request.POST == POST:
        print(POST)
        try:
            entry_map = {NAME: request.POST.get(NAME),
                         STOCK: request.POST.get(STOCK)}
            append_creation_details(entry_map,ADDED_AT)
            record = getattr(
                models, BOOK_STORE_TABLE).objects.update_or_create(**entry_map)
            data = {RESPONSE: SUCCESS}
        except Exception as ex:
            data = {RESPONSE: FAILURE}
        return JsonResponse(data, safe=False)
    return render(request, BASE_MODAL_PATH, {INPUT_PATH:CREATE_PATH})


def delete(request, book_id):
    if request.POST == POST:
        print(POST)
        try:
            record = getattr(models, BOOK_STORE_TABLE).objects.get(
                pk=book_id).delete()
            data = {RESPONSE: SUCCESS}
        except Exception as ex:
            data = {RESPONSE: FAILURE}
        return JsonResponse(data, safe=False)
    return render(request,  BASE_MODAL_PATH, {INPUT_PATH:DELETE_PATH})


def view(request, book_id):
    record = getattr(models, BOOK_STORE_TABLE).objects.get(pk=book_id)
    return render(request, BASE_MODAL_PATH, {INPUT_PATH:VIEW_PATH})


def update(request, book_id):
    if request.POST == POST:
        print(POST)
        try:
            record = getattr(models, BOOK_STORE_TABLE).objects.get(pk=book_id)
            stock = request.POST.get(STOCK)
            setattr(record, STOCK, int(stock))
            setattr(record, MODIFIED_AT, datetime.datetime.now())
            record.save()
            data = {RESPONSE: SUCCESS}
        except Exception as ex:
            data = {RESPONSE: FAILURE}
        return JsonResponse(data, safe=False)

    record = getattr(models, BOOK_STORE_TABLE).objects.get(pk=book_id)
    return render(request, BASE_MODAL_PATH, {INPUT_PATH:CREATE_PATH})


def search(request, query):
    request.POST
    response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
    data= {}
    return JsonResponse(data,safe=False)

def append_creation_details(entry_map, key):
    entry_map[key] = datetime.datetime.now()
