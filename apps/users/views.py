from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
# Create your views here.
from .models import UsersModel
from .serializers import RegisterUserModelSerializer, CountUserModelSerializer


class UserViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    create: 用户注册接口
    list: 用户注册验重用户名，邮箱接口
    """
    queryset = UsersModel.objects.all()
    serializer_class = RegisterUserModelSerializer

    def count(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=kwargs)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == repr('count'):
            return CountUserModelSerializer
        return self.serializer_class
