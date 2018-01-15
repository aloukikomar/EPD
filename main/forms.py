from django import forms
from main.models import panelpost

class AddPost(forms.ModelForm):
    class Meta():
        model = panelpost
        fields =['Username','College','Title','Type','Subject','Branch','DDate','Markslow12','Markslowb','Pack','Training']
        widgets = {'Username' : forms.TextInput(attrs={'class':'fieldadd s'}),
        'College' : forms.TextInput(attrs={'class':'fieldadd s'}),
        'Title' : forms.TextInput(attrs={'class':'fieldadd l'}),
        'Type' : forms.TextInput(attrs={'class':'fieldadd s'}),
        'Subject' : forms.TextInput(attrs={'class':'fieldadd xl'}),
        'Branch' : forms.TextInput(attrs={'class':'fieldadd s'}),
        'Markslow12' : forms.TextInput(attrs={'class':'fieldadd s'}),
        'Markslowb' : forms.TextInput(attrs={'class':'fieldadd s'}),
        'Pack' : forms.TextInput(attrs={'class':'fieldadd s'}),        
        'Training' : forms.TextInput(attrs={'class':'fieldadd s'})
        }
