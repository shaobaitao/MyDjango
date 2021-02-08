from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("This is tow index")


def renderTest(request):
    return render(request,'render.html')


def renderTestTwo(request):
    return render(request,'testRenderTwo.html')