from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import userform


def aboutus(request):
    if request.method=='GET':
        output=request.GET.get('output')
    return render(request,"about.html",{'output':output})
def submitForm(request):
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

           return HttpResponse(finalans)
    except:
        pass
   

def userForm(request):
    fn=userform()
    data={'forms':fn}
    try:
        if request.method=='POST':
        # n1=request.GET['num1']
        # n2=request.GET['num2']
           n1=int(request.POST.get('num1'))
           n2=int(request.POST.get('num2'))
           finalans=n1+n2
           data={
               'form':fn,
               'n1':n1,
               'n2':n2,
               'output':finalans
           }
           url="/aboutus/?output={}".format(finalans)

           return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"userForm.html",data)
   



def homePage(request):
    return render(request, "index.html")
