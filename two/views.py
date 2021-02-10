from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    return HttpResponse("This is tow index")


def renderTest(request):
    return render(request, 'render.html')


def renderTestTwo(request):
    context = {
        'list': [100, 90, 80, 70],
        'name': 'sbt'
    }
    return render(request, 'testRenderTwo.html', context=context)


def renderBase(request):
    # render的底层实现分为两步
    #  （1）加载

    index = loader.get_template('renderBase.html')
    context = {
        'name': 'sbt'
    }
    #  （2）渲染
    result = index.render(context=context)
    return HttpResponse(result)
