from django.shortcuts import render
from main import forms
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    return render(request, 'main/main.html')

def notification(request):
    return render(request, 'main/notification.html')

def clist(request):
    return render(request, 'main/clist.html')

def addpost(request):
    template_name = 'main/admini.html'
    add = forms.AddPost()
    if request.method == 'POST' and 'Add' in request.POST:
        add = forms.AddPost(request.POST)
        add.save(commit=True)
        if add:
            return HttpResponseRedirect(reverse('index'))
        else:
             return HttpResponse('Failed')      
    return render(request,template_name, {'add':add})