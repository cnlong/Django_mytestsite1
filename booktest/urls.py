from django.urls import path
from booktest import views

urlpatterns = [
    path('index', views.index),  # 图书信息页面
    path('create', views.create),  # 新增一本新书
    path('delete<int:bid>', views.delete),  # 删除一本书
    path('areas', views.areas),
]
