import datetime

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render

import inventory.models as models
from .constants import *

def index(request):
    if request.method == POST:
        print(POST)
    records = getattr(models, BOOK_STORE_TABLE).objects.all();
    return render(request, BASE_PATH, {ENTRIES:records})


def add(request):
    if request.method == POST :
        print(POST)
        print(request.POST)
        try:
            entry_map = {NAME: request.POST.get(NAME),
                         STOCK: request.POST.get(STOCK),
                         BOOK_ID:request.POST.get(BOOK_ID)}
            append_creation_details(entry_map,ADDED_AT)
            print(entry_map)
            record = getattr(
                models, BOOK_STORE_TABLE).objects.update_or_create(**entry_map)
            data = {RESPONSE: SUCCESS}
        except Exception as ex:
            print(ex)
            data = {RESPONSE: FAILURE}
        return JsonResponse(data, safe=False)
    return render(request, BASE_MODAL_PATH, {INPUT_PATH:CREATE_PATH})


def delete(request, book_id):
    if request.method == POST:
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
    print(book_id,request.GET)
    record = getattr(models, BOOK_STORE_TABLE).objects.get(pk=book_id)
    return render(request, BASE_MODAL_PATH, {INPUT_PATH:VIEW_PATH,SELECTED:record})


def update(request, book_id):
    if request.method == POST:
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
    return render(request, BASE_MODAL_PATH, {INPUT_PATH:CREATE_PATH,SELECTED:record})


def append_creation_details(entry_map, key):
    entry_map[key] = datetime.datetime.now()
