from django import forms
from app.models import *
from django.core import validators

def validate_for_a(data):
    if data.lower().startswith('c'):
        raise forms.ValidationError('starts with c')

    
    
class TopicForm(forms.Form):
    n1=[[no.Topic_Name,no.Topic_Name] for no in Topic.objects.all()]
    Topic_Name=forms.CharField(validators=[validate_for_a])

class WebpageForm(forms.Form):
    t1=[[to.Topic_Name,to.Topic_Name] for to in Webpage.objects.all()]
    Topic_Name=forms.CharField(validators=[validate_for_a,validators.MinLengthValidator(5)])
    Name=forms.CharField()
    Url=forms.URLField()
    Email=forms.EmailField()
    Reenter_Email=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('BOT')


    def clean(self):
        e=self.cleaned_data['Email']
        re=self.cleaned_data['Reenter_Email']
        if e!=re:
            raise forms.ValidationError('email is not matched')

