from django import forms
from main.models import panelpost,List

class AddPost(forms.ModelForm):
    class Meta():
        model = panelpost
        fields =['Username','College','Title','Type','Subject','Branch','DDate','Markslow12','Markslowb','Pack','Training']
        widgets = {'Username' : forms.TextInput(attrs={'class':'fieldadd l'}),
        'College' : forms.TextInput(attrs={'class':'fieldadd l'}),
        'Title' : forms.TextInput(attrs={'class':'fieldadd l'}),
        'Branch' : forms.Select(attrs={'class':'fieldadd l'}),
        'Subject' : forms.Textarea(attrs={'class':'fieldadd xl'}),
        'Type' : forms.Select(attrs={'class':'fieldadd s'}),
        'Markslow12' : forms.NumberInput(attrs={'class':'fieldadd s'}),
        'Markslowb' : forms.NumberInput(attrs={'class':'fieldadd s'}),
        'Pack' : forms.NumberInput(attrs={'class':'fieldadd s'}),        
        'Training' : forms.NumberInput(attrs={'class':'fieldadd s'})
        }

class AddList(forms.ModelForm):
    class Meta():
        model = List
        fields =['ListName','College','Branch','Date','Markslow12','Markslowb','Markslowc']
        widgets = {'ListName' : forms.TextInput(attrs={'class':'fieldadd l'}),
        'College' : forms.TextInput(attrs={'class':'fieldadd l'}),
        'Branch' : forms.Select(attrs={'class':'fieldadd l'}),
        'Markslow12' : forms.NumberInput(attrs={'class':'fieldadd s'}),
        'Markslowb' : forms.NumberInput(attrs={'class':'fieldadd s'}),
        'Markslowc' : forms.NumberInput(attrs={'class':'fieldadd s'})
        }
