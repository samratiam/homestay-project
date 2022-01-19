from django.shortcuts import render

# Create your views here.

from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path("",TemplateView.as_view(template_name="homes/home.html"),{})
]

    