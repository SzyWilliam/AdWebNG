from django.urls import path

from . import views

from qa.services.system import account

urlpatterns = [
    path('', views.index, name='index'),
    # --系统模块--
    # 用户注册
    path('system/register', account.user_register, name='register'),
    # 登录
    path('system/login', account.user_login, name='login'),
    # 登出
    path('system/logout', account.user_logout, name='logout'),

    path('test', account.test, name='test'),

]
