from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from two.models import Animals


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


def create(request):
    animal = Animals()
    animal.name = 'lizard'
    animal.age = 3
    animal.save()
    return HttpResponse('create success')


def retrieve(request):
    list = Animals.objects.all()
    for a in list:
        print(a.id,a.age,a.name)
    return HttpResponse(list)


def delete(request):
    animal = Animals.objects.get(pk=2)
    animal.delete()
    return HttpResponse('delete success')


def update(request):
    animal = Animals.objects.get(pk=1)
    animal.name = 'marmot'
    animal.age = 10
    animal.save()

    return HttpResponse('update success')