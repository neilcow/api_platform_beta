from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from utils.base.base_views import BaseViews


class InterfacesViewSet(BaseViews, ModelViewSet):
    """
    list: 接口列表
    create: 创建接口
    read: 接口详情
    update: 全量更新
    partial_update: 部分更新
    delete: 删除接口
    configures: 接口下配置的id和name列表
    testcases: 接口下用例的id和name列表
    """