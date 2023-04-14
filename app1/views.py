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