from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("This is tow index")


def renderTest(request):
    return render(request,'render.html')


def renderTestTwo(request):
    context={
        'list':[100,90,80,70],
        'name':'sbt'
    }
    return render(request,'testRenderTwo.html',context=context)