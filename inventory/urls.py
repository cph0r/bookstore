from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<str:book_id>/', views.add, name='add'),
    path('delete/<str:book_id>/', views.delete, name='delete'),
    path('view/<str:book_id>/', views.view, name='view'),
]