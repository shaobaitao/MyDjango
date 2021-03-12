from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def setSess(request):
    username = 'shaobaitao'
    request.session['username'] = username

    return HttpResponse('ok')


def getSess(request):
    username = request.session.get('username')
    return render(request, 'getSess.html', context=locals())
