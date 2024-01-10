from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse


# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['Topic_Name']
            TO=Topic.objects.get_or_create(Topic_Name=tn)[0]
            TO.save()
            return HttpResponse('topic created')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_topic.html',d)        

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['Topic_Name']
            n=WFDO.cleaned_data['Name']
            u=WFDO.cleaned_data['Url']
            e=WFDO.cleaned_data['Email']
            re=WFDO.cleaned_data['Reenter_Email']
            TO=Topic.objects.get(Topic_Name=tn)
            WO=Webpage.objects.get_or_create(Topic_Name=TO,Name=n,Url=u,Email=e)[0]
            WO.save()
            return HttpResponse('webpage created')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_webpage.html',d)        




            