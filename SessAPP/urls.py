from django.conf.urls import url

from SessAPP import views

urlpatterns = [
    url(r'^setSess', views.setSess),
    url(r'^getSess', views.getSess),
]
