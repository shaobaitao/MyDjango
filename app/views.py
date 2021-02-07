from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    import datetime
    return HttpResponse(datetime.datetime.now())
