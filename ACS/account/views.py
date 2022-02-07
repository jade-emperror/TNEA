import email
from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.
def test(request):
    return render(request,'home.html')

def login(request):
    if(request.method == 'GET'):
        return render(request,'login.html')
    else:
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        if(models.user.objects.filter(email=email,pwd=pwd).exists()):
            user_obj=models.user.objects.get(email=email)
            request.session['isLogin'] = True
            request.session['id']= user_obj.id
            request.session['mail'] = user_obj.email
            request.session.set_expiry(0)
            return render(request,'dashboard.html')
        else:
            return render(request,'login.html',{'flag':True,'msg':"username or password is invalid"})

def signup(request):
    if(request.method == 'GET'):
        return render(request,'signup.html')
    else:
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        if(models.user.objects.filter(email=email).exists()):
            return HttpResponse("user exists")
        else:
            models.user.objects.create(fname=fname,lname=lname,email=email,pwd=pwd).save()
            return render(request,'login.html',{'flag':True,'msg':"Login here"})