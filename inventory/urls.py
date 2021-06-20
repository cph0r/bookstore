from django.urls import path

from . import views


app_name = 'inventory'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('update/<str:book_id>/', views.update, name='update'),
    path('delete/<str:book_id>/', views.delete, name='delete'),
    path('view/<str:book_id>/', views.view, name='view'),
]