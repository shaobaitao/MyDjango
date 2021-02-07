from django.conf.urls import url

from two import views

urlpatterns={
    url(r'^index/', views.index),
}