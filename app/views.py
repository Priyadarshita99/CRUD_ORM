from django.shortcuts import render

# Create your views here.

from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

def display_topic(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())
    QLTO=Topic.objects.all()
    
    d={'Topics':QLTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('topic_name')
    QLWO=Webpage.objects.all().order_by(Length('topic_name'))
    QLWO=Webpage.objects.exclude(name='BB')
    QLWO=Webpage.objects.filter(name='PR')
    QLWO=Webpage.objects.filter(name__endswith='i')
    QLWO=Webpage.objects.filter(pk='1',name='Kohli')
    #QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(Q(pk='1') & Q(name='Kohli'))
    QLWO=Webpage.objects.filter(Q(name='Kohli') | Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(name__regex=r'PR')
    QLWO=Webpage.objects.filter(name__regex=r'\wi$')
    QLWO=Webpage.objects.filter(name__regex=r'^P')
    QLWO=Webpage.objects.all()
    
    
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    QLAO=Accessrecord.objects.all()
    QLAO=Accessrecord.objects.all().order_by('author')
    QLAO=Accessrecord.objects.filter(id__gt=3)
    QLAO=Accessrecord.objects.filter(date__year='2022')
    QLAO=Accessrecord.objects.filter(date__year__gt='2022')
    QLAO=Accessrecord.objects.filter(date__day='19')                #date
    QLAO=Accessrecord.objects.filter(pk__in=[3,6])                  #(3,6)
    QLAO=Accessrecord.objects.filter(author__startswith='M')            
    #QLAO=Accessrecord.objects.filter(name__endswith='M')     #not getting coz name column is a foreignkey
    QLAO=Accessrecord.objects.filter(author__contains='r')
    QLAO=Accessrecord.objects.all().order_by('pk')[:3]
    QLAO=Accessrecord.objects.all()

    d={'Access':QLAO}
    return render(request,'display_accessrecord.html',d)

#insert data by cmd
def insert_topic(request):
    tn=input('enter topic name')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()

    return render(request,'display_topic.html')


def insert_webpage(request):
    wo=input('enter the topicname ')
    n=input()
    u=input()

    WO=Topic.objects.get(topic_name=wo)
    NWO=Webpage.objects.get_or_create(topic_name=WO,name=n,url=u)[0]
    NWO.save()

    return render(request,'display_webpage.html')

def insert_accessrecord(request):
    ao=int(input())
    #n=input('enter the name ')
    a=input('enter the author name ')
    d=input('enter the date ')

    ARO=Webpage.objects.get(pk=ao)
    NARO=Accessrecord.objects.get_or_create(name=ARO,author=a,date=d)[0]
    NARO.save()

    return render(request,'display_accessrecord.html')

def update_webpage(request):

    #update-one row & more rows ..Update   #No row...won't  do anything
    #Webpage.objects.filter(topic_name=3).update(name='Rohan')#not specified topic_name as PK so t_n=number
    #Webpage.objects.filter(name='kb').update(topic_name=1)  #1=Cricket
    #Webpage.objects.filter(name='FF').update(url='https://ffupd.in')

    #update_or_create-one row..Update #No row..create  #more rows..Error
    #FBO=Topic.objects.get_or_create(topic_name='FB')[0]
    #Webpage.objects.update_or_create(name='kb',defaults={'topic_name':FBO})

    VBO=Topic.objects.get_or_create(topic_name='Volley Ball')[0]            #New t_n added
    Webpage.objects.update_or_create(name='kb',defaults={'topic_name':VBO})

    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def delete_accessrecord(request):
    #Accessrecord.objects.filter(author='kkk').delete()
    Accessrecord.objects.filter(name=4).delete() #Webapge's pk-4..Rohan,So deleted Rohan from AR-table

    QLAO=Accessrecord.objects.all()
    d={'Access':QLAO}
    return render(request,'display_accessrecord.html',d)

