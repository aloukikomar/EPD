from django import forms
from login.models import UserMain

class LoginForm(forms.Form):
    UserId = forms.CharField(widget=forms.TextInput(attrs={'class':'loginput'}))
    UserPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'loginput'}))

class RegistrationForm1(forms.ModelForm):
    class Meta():
        model = UserMain
        fields =['UserName','Password','Type','College','Email','Pno']
        widgets = {'UserName' : forms.TextInput(attrs={'class':'loginput'}),
        'Password' : forms.PasswordInput(attrs={'class':'loginput'}),
        'Type' : forms.TextInput(attrs={'class':'loginput'}),
        'College' : forms.TextInput(attrs={'class':'loginput'}),
        'Email' : forms.EmailInput(attrs={'class':'loginput'}),
        'Pno' : forms.NumberInput(attrs={'class':'loginput'}),
        'BDate' : forms.DateInput(attrs={'class':'loginput'}),
        }
