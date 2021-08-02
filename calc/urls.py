from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('calc', views.home, name='home'),
    path('add', views.add, name= 'add')
]
