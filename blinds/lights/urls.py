from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('state/', views.stateData, name='state'),
    path('set/', views.edit, name='Edit'),
]
