from django.conf.urls import url

from two import views

urlpatterns = {
    # 视图函数的返回值---字符串
    url(r'^index/', views.index),

    # 试图函数的返回值---页面
    url(r'^renderTest/', views.renderTest),

    # two下的模板
    url(r'^renderTestTwo', views.renderTestTwo),

    # render底层
    url(r'^renderBase',views.renderBase),

    # mysql
    url(r'^mysqlAdd',views.mysqlAdd),
}
