from django.shortcuts import render

# Create your views here.
def senddata(request):
    d={'name':'pravee','age':23}
    return render(request,'senddata.html',context=d)