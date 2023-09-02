from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app1.models import To_Do_data




def home(req):
    data1=To_Do_data.objects.all()
    return render(req,'index.html',{'data':data1})


def save_data(req):
    if req.method=="POST":
        title=req.POST.get('title')
        desc=req.POST.get('desc')
        print(title,desc)

        data=To_Do_data(title=title,desc=desc)
        data.save()

        data1=To_Do_data.objects.all()
       
        return HttpResponseRedirect('/',{'data':data1})
    
    else:
        data1=To_Do_data.objects.all()
        return HttpResponseRedirect('/',{'data':data1})


def Remove_data(req,id):
    data=To_Do_data.objects.get(pk=id)
    data.delete()

    data1=To_Do_data.objects.all()
    return HttpResponseRedirect('/',{'data':data1})