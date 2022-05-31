from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from utils.base.base_views import BaseViews


class ProjectsViewSet(BaseViews, ModelViewSet):
    """
      list: 项目列表
      create: 创建项目
      names: 项目的id和name列表
      read: 项目详情
      update: 全量更新
      partial_update: 部分更新
      delete: 删除项目
      interfaces: 项目下接口的id和name列表
      """

