

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from utils.constant.serializer_attr_constant import LABEL, HELP_TEXT, MIN_LENGTH, MAX_LENGTH, VALIDATORS, WRITE_ONLY, \
    REQUIRED
from utils.user_utils import generate_token

from .constant import SerializerFieldsConstant
from .models import UsersModel


class RegisterUserModelSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(label="确认密码", help_text="确认密码", min_length=6, max_length=20,
                                             write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = UsersModel
        fields = (SerializerFieldsConstant.ID_FIELD,
                  SerializerFieldsConstant.USERNAME_FIELD,
                  SerializerFieldsConstant.PASSWORD_FIELD,
                  SerializerFieldsConstant.PASSWORD_CONFIRM_FIELD,
                  SerializerFieldsConstant.EMAIL_FIELD,
                  SerializerFieldsConstant.TOKEN_FIELD
                  )

        extra_kwargs = {
            SerializerFieldsConstant.USERNAME_FIELD: {
                LABEL: "用户名",
                HELP_TEXT: "用户名",
                MIN_LENGTH: 6,
                MAX_LENGTH: 20,
                VALIDATORS: [UniqueValidator(queryset=UsersModel.objects.all())]
            },
            SerializerFieldsConstant.PASSWORD_FIELD: {
                LABEL: "密码",
                HELP_TEXT: "密码",
                MIN_LENGTH: 6,
                MAX_LENGTH: 20,
                WRITE_ONLY: True
            },
            SerializerFieldsConstant.EMAIL_FIELD: {
                LABEL: "邮箱",
                HELP_TEXT: "邮箱",
                REQUIRED: True,
                WRITE_ONLY: True,
                VALIDATORS: [UniqueValidator(queryset=UsersModel.objects.all())]
            },
        }

        def validate(self, attrs: dict):
            if attrs.get(SerializerFieldsConstant.PASSWORD_FIELD) != attrs.get(
                    SerializerFieldsConstant.PASSWORD_CONFIRM_FIELD):
                raise serializers.ValidationError("两次输入密码不一致！")
            return attrs

        def create(self, validated_data: dict):
            # 给密码加密
            password = validated_data.get(SerializerFieldsConstant.PASSWORD_FIELD)
            validated_data.pop(SerializerFieldsConstant.PASSWORD_CONFIRM_FIELD)
            validated_data[SerializerFieldsConstant.PASSWORD_FIELD] = make_password(password)
            # 数据库创建用户数据
            user = super().create(validated_data)
            # 生成token
            token = generate_token(user=user)
            # 返回值添加token属性
            user.token = token
            return user


class CountUserModelSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = UsersModel
        fields = (SerializerFieldsConstant.USERNAME_FIELD,
                  SerializerFieldsConstant.EMAIL_FIELD,
                  SerializerFieldsConstant.COUNT_FIELD)

        extra_kwargs = {
            SerializerFieldsConstant.USERNAME_FIELD: {
                LABEL: "用户名",
                HELP_TEXT: "用户名",
                REQUIRED: False,
                VALIDATORS: []
            },
            SerializerFieldsConstant.EMAIL_FIELD: {
                LABEL: "邮箱",
                HELP_TEXT: "邮箱",
                VALIDATORS: []
            },
        }

    def validate(self, attrs):
        username = attrs.get(SerializerFieldsConstant.USERNAME_FIELD)
        email = attrs.get(SerializerFieldsConstant.EMAIL_FIELD)
        if username:
            user = UsersModel.objects.filter(username__exact=username)
            attrs[SerializerFieldsConstant.COUNT_FIELD] = user.count()
        else:
            email = UsersModel.objects.filter(email__exact=email)
            attrs[SerializerFieldsConstant.COUNT_FIELD] = email.count()
        return attrs

