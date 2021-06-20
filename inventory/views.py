import datetime

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
import inventory.models as models
from .constants import *
import requests

def index(request):
    records = getattr(models, BOOK_STORE_TABLE).objects.all();
    return render(request, BASE_PATH, {ENTRIES:records})


def add(request):
    if request.method == POST :
        book_id = request.POST.get(BOOK_ID)
        count = getattr(
                models, BOOK_STORE_TABLE).objects.filter(**{BOOK_ID:book_id}).count()
        if count > 0:
            messages.error(request,DUPLICATE)
        else:
            entry_map = {NAME: request.POST.get(NAME),
                        STOCK: request.POST.get(STOCK),
                        BOOK_ID:book_id,ADDED_AT:datetime.datetime.now()}
            getattr(
                models, BOOK_STORE_TABLE).objects.update_or_create(**entry_map)
            messages.success(request,SUCCESS)
        return redirect(MAIN_VIEW)
    return render(request, BASE_MODAL_PATH, {INPUT_PATH:CREATE_PATH})


def delete(request, book_id):
    if request.method == POST:
        try:
            getattr(models, BOOK_STORE_TABLE).objects.get(
                pk=book_id).delete()
            messages.success(request,SUCCESS)
        except Exception as ex:
            messages.error(request,ERROR)
        return redirect(MAIN_VIEW)
    return render(request,  BASE_MODAL_PATH, {INPUT_PATH:DELETE_PATH,BOOK_ID:book_id})


def view(request, book_id):
    record = getattr(models, BOOK_STORE_TABLE).objects.get(pk=book_id)
    active_fields = {INPUT_PATH:VIEW_PATH,SELECTED:record}
    update_active_fields(record, active_fields)
    return render(request, BASE_MODAL_PATH, active_fields)


def update(request, book_id):
    if request.method == POST:
        book_id_2 = request.POST.get(BOOK_ID)
        try:
            getattr(models, BOOK_STORE_TABLE).objects.all().exclude(pk=book_id).get(**{BOOK_ID:book_id_2})
            messages.error(request,DUPLICATE)
        except Exception as ex:
            print(ex)
            record = getattr(models, BOOK_STORE_TABLE).objects.get(pk=book_id)
            name = request.POST.get(NAME)
            stock = request.POST.get(STOCK)
            setattr(record, NAME, name)
            setattr(record, BOOK_ID, book_id_2)
            setattr(record, STOCK, int(stock))
            setattr(record, MODIFIED_AT, datetime.datetime.now())
            record.save()
            messages.success(request,SUCCESS)
        return redirect(MAIN_VIEW)
    record = getattr(models, BOOK_STORE_TABLE).objects.get(pk=book_id)
    active_fields = {INPUT_PATH:CREATE_PATH,SELECTED:record}
    update_active_fields(record, active_fields)
    return render(request, BASE_MODAL_PATH, active_fields)

def update_active_fields(record, active_fields):
    master_book_id = getattr(record,BOOK_ID)
    result = requests.get('https://www.googleapis.com/books/v1/volumes/'+master_book_id)
    result = result.json()
    active_fields.update({
    'author' : result['volumeInfo']['authors'][0],
    'publisher' : result['volumeInfo']['publisher'],
    'publishing_date' : result['volumeInfo']['publishedDate'],
    'page_count' :result['volumeInfo']['pageCount'],
    'thumbnail' : result['volumeInfo']['imageLinks']['smallThumbnail'],
    'language' : result['volumeInfo']['language'].upper() })
