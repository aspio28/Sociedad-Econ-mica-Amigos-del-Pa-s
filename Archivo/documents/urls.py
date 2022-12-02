from django.urls import path
from . import views

urlpatterns = [
    path('new', views.New_Document, name='document_new'),
]