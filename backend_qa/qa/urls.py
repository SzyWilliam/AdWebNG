from django.urls import path

from . import views

from qa.services import kg

urlpatterns = [
    path('', views.index, name='index'),
    # 查询
    path('kg/query', kg.query, name='query'),
    # 删除
    path('kg/delete', kg.delete, name='delete'),
    # 修改
    path('kg/update', kg.update, name='update'),
    # 新增
    path('kg/insert', kg.insert, name='insert'),

    # path('test', account.test, name='test'),

]
