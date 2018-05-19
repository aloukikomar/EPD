from django.conf.urls import url
from login import views


urlpatterns =[
    url(r'^/', views.landing , name='landing'),
    url(r'^login/', views.landing, name='landing'),
    url(r'^reg/', views.reg, name='reg')]

