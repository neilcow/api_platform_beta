from django.conf.urls import url
from django.urls import re_path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    url('register/', views.UserViewSet.as_view({"post": "create"})),
    url('login/', obtain_jwt_token),
    re_path(r'^(?P<email>[A-Za-z0-9]*@([A-Za-z0-9\-]+\.)+[A-Za-z]{2,6})/count',
            views.UserViewSet.as_view({"get": repr('count')})),
    url(r'^(?P<username>\w*)/count', views.UserViewSet.as_view({"get": repr('count')}))
]