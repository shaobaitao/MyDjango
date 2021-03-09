from django.conf.urls import url

from CookAPP import views

urlpatterns = [
    url(r'^toCookiesLogin', views.toCookieLogin),
    url(r'^cookieLogin/', views.cookieLogin, name='cookieLogin'),
    url(r'^cookieWelcome/', views.cookieWelcome, name='cookieWelcome'),
    url(r'^cookieLogout/', views.cookieLogout,name='cookieLogout')
]
