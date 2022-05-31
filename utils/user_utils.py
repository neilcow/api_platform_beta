"""
 @Time : 2021/3/6 18:11
 @Author : tango
 @FileName: user_utils.py
 @Software: PyCharm
 @E-mail : 13012830533@163.com
 @Description: 
"""
from django.contrib.auth.hashers import make_password
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from users.models import UsersModel


def generate_token(user: UsersModel):
    """
    调用rest_framework_jwt中的方法，生成jwt token，可以在全局配置中使用：JWT_EXPIRATION_DELTA配置过期时间
    :param user: UsersModel的实例
    :return:
    """
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)
