from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from main.models import panelpost,Notification
from main import views
urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^notification/', ListView.as_view(queryset=Notification.objects.all().order_by("-Date"), template_name="main/notification.html"), name='notice'),
    url(r'^administration/', views.addpost, name='administration'),
    url(r'^view/', ListView.as_view(queryset=panelpost.objects.all().order_by("-Date"), template_name="main/viewpanel.html"),name='view'),
    url(r'^list/', views.clist, name='clist')
   ]
 