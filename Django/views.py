from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return HttpResponse("About Us page 1")


def userForm(request):
    try:
        # n1=request.GET['num1']
        # n2=request.GET['num2']
        n1=request.GET.get('num1')
        n2=request.GET.get('num2')
        print(n1+n2)
    except:
        pass
    return render(request,"userForm.html")

def index(request):
    return render(request,"about.html")

def homePage(request):
    return render(request, "index.html")
