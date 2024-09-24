from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return HttpResponse("About Us page 1")


def userForm(request):
    data={}
    try:
        if request.method=='POST':
        # n1=request.GET['num1']
        # n2=request.GET['num2']
           n1=int(request.POST.get('num1'))
           n2=int(request.POST.get('num2'))
           finalans=n1+n2
           data={
               'n1':n1,
               'n2':n2,
               'output':finalans

           }
    except:
        pass
    return render(request,"userForm.html",data)

def index(request):
    return render(request,"about.html")

def homePage(request):
    return render(request, "index.html")
