from django.http import response
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def toCookieLogin(request):
    return render(request, 'cookieLogin.html')


def cookieLogin(request):
    name = request.POST.get('name')
    myResponse = redirect(reverse('cook:cookieWelcome'))
    myResponse.set_cookie('name', name)

    return myResponse


def cookieWelcome(request):
    name = request.COOKIES.get('name', '游客')

    return render(request, 'cookieWelcome.html', context=locals())


def cookieLogout(request):
    myResponse = redirect(reverse('cook:cookieWelcome'))
    myResponse.delete_cookie('name')
    return myResponse
