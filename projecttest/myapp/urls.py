from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),

    
]
