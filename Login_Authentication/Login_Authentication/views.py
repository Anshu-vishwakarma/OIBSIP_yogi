from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register_form(req):
    
     if req.method == "POST":
      print("POST_Method")
      fm=UserCreationForm(req.POST)
      if fm.is_valid():
         fm.save()
         return HttpResponse("<h1> Registration Sucessfuly  </h1> ")
     else:
       fm=UserCreationForm()
     return render(req,'index.html',{'form':fm})



    
    # return render(req,'index.html')



def Login_Form(req):
    if req.method =="POST":
        username=req.POST.get('username')
        password=req.POST.get('password')
        
        user=authenticate(username=username,password=password)
        if user is not None:
           login(req,user)
           return HttpResponse("<h1> Welcome , You are logined...  </h1>")
        else:
           msg= messages.error(req,"Invalid User & Password")
           print(msg)
           return render(req,'Login.html',{'msg':msg})


        return HttpResponse("save")
    else:

     return render(req,'Login.html')