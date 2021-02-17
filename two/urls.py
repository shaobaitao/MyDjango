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
    url(r'^renderBase', views.renderBase),

    # mysql CURD
    url(r'^create', views.create),
    url(r'^retrieve', views.retrieve),
    url(r'^delete', views.delete),
    url(r'^update', views.update),

    # mysql 一对多查询
    url(r'^getDogs', views.getDogs),
    url(r'^getAnimals', views.getAnimals),

    # fitter exclude查询
    url(r'^fitter', views.fitter),

    # 带参数请求
    url(r'^courses',views.course),
    url(r'^students',views.students),

    # 4 methods of create objects
    url(r'^createObjects',views.createObjects),
}
