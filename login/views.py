from django.shortcuts import render
from login import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
def index(request):
    template_name = 'login/index.html'
    return render(request,template_name)
def landing(request):
    template_name = 'login/index.html'
    logform = forms.LoginForm()
    regform1 = forms.RegistrationForm1() 
    if request.method=='POST' and 'Log' in request.POST:
        UserId = request.POST.get('UserId') 
        UserPassword = request.POST.get('UserPassword') 
        user = authenticate(UserId=UserId,UserPassword=UserPassword)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("failed")
        
    if request.method=='POST' and 'Reg' in request.POST:
        regform1 = forms.RegistrationForm1(request.POST)
        regform1.save(commit=True)
        return index(request)     
    return render(request,template_name, { 'logform':logform, 'regform1':regform1})