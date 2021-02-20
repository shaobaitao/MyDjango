from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from two.models import Animals, Courses, Students
from two.models import Dogs


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

    t = loader.get_template('renderBase.html')
    context = {
        'name': 'sbt'
    }
    #  （2）渲染
    result = t.render(context=context)
    return HttpResponse(result)


def create(request):
    animal = Animals()
    animal.name = 'lizard'
    animal.age = 3
    animal.save()
    return HttpResponse('create success')


def retrieve(request):
    animals = Animals.objects.all()
    for a in animals:
        print(a.id, a.age, a.name)
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


# 知道动物类别的id 查此类别所有动物的名字
def getDogs(request):
    animals = Animals.objects.get(id=3)
    dogs = animals.dogs_set
    dogList = []
    for dog in dogs.all():
        dogList.append(dog.name)
    return HttpResponse(dogList)


# 知道动物的名字 查此类别动物的id
def getAnimals(request):
    dogs = Dogs.objects.get(name='lisa')
    return HttpResponse(dogs.fk.name)


def fitter(request):
    animals = Animals.objects.filter(name__contains='m')
    data = {}
    for i, animal in enumerate(animals):
        data[i] = animal.name
        # data[index]['id'] = animal.id
    return JsonResponse(data)


def course(request):
    courses = Courses.objects.all()

    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context=context)


def students(request):
    courseId = request.GET.get('id')

    student = Students.objects.filter(course_id=courseId)

    context = {
        'students': student
    }
    return render(request, 'students.html', context=context)


def createObjects(request):
    courses = Courses()
    courses.name = 'UI'
    courses.save()
    return HttpResponse('create object success')


def orderBy(request):
    courses = Courses.objects.order_by('num')
    for i in courses:
        print(i.id, i.name, i.num)
    return HttpResponse('order by success')


def getOne(request):
    # animal = Animals.objects.first()

    # animal = Animals.objects.last()

    # animal = Animals.objects.exists()
    # animal = Animals.objects.filter(name='lizard')
    # if animal.exists():
    #     print(animal exist)
    # else:
    #     print(animal not exist)

    animal = Animals.objects.filter(name='lizard').count()
    print(animal)
    return HttpResponse('get one success')
