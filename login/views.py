from django.shortcuts import render
from login import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from login.querry import auth
from login.models import UserMain

def index(request):
    template_name = 'login/loginform.html'
    return render(request,template_name)
def landing(request):
    template_name = 'login/loginform.html'
    logform = forms.LoginForm()
    if request.method =='POST' or 'Log' in request.POST:
        name=request.POST.get('UserId')
        passw=request.POST.get('UserPassword') 
        n=auth(name,passw)
        if n != None:
              request.session['id'] = name
              return render(request, 'main/main.html',{'seId':request.session.get('id')})
        else:
            return render(request,template_name, { 'logform':logform,'message':"User id or password is wrong"})
       
    return render(request,template_name, { 'logform':logform})   

def reg(request):       
    regform1 = forms.RegistrationForm1() 
    template_name = 'login/regform.html'
    if request.method=='POST' and 'Reg' in request.POST:
        regform1 = forms.RegistrationForm1(request.POST)
        regform1.save(commit=True)
        return landing(request)     
    return render(request,template_name, {'regform1':regform1})