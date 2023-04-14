from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse('topic insertion successfully')
    return render(request,'insert_topic.html')





def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST.get('url')
        email=request.POST['email']
        TO=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('webpage insertion is done Successfully')


    return render(request,'insert_webpage.html',d)

