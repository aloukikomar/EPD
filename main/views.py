from django.shortcuts import render
from main import forms
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from main.querry import lidata,result
from login.querry import mlist

def index(request):
    return render(request, 'main/main.html')

def notification(request):
    return render(request, 'main/notification.html')

def glist(request):
    new=str(request)
    listid=result(new[31:-2]) 
    return render(request, 'main/list.html',{'listid':listid})

def addpost(request):
    template_name = 'main/admini.html'
    addp = forms.AddPost()
    addl = forms.AddList()
    if request.method == 'POST' and 'Addp' in request.POST:
        addp = forms.AddPost(request.POST)
        addp.save(commit=True)
        if addp:
            return HttpResponseRedirect(reverse('index'))
        else:
             return HttpResponse('Failed')  
    elif request.method == 'POST' and 'Addl' in request.POST:
        addl = forms.AddList(request.POST)
        addl.save(commit=True)
        if addl:
            return HttpResponseRedirect(reverse('index'))
        else:
             return HttpResponse('Failed')       
    return render(request,template_name, {'addp':addp,'addl':addl})