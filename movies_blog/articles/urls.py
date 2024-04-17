from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('detail/<int:pk>/', views.detail, name = 'detail'),
    path('create/', views.create, name = 'create'),
    path('save/', views.save, name='save'),
    path('edit/<int:pk>', views.edit, name = 'edit'),
]