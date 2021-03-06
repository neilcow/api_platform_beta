"""
Django settings for api_platform_beta project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import datetime
from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 设置apps为资源路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*mp2((_u)$&jc^dl(ccwn6hh&=1*k^mzcy^n@a8l9$#m#db^w)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'configures.apps.ConfiguresConfig',
    'debugtalks.apps.DebugtalksConfig',
    'envs.apps.EnvsConfig',
    'interfaces.apps.InterfacesConfig',
    'projects.apps.ProjectsConfig',
    'reports.apps.ReportsConfig',
    'testcases.apps.TestcasesConfig',
    'testsuites.apps.TestsuitesConfig',
    'users.apps.UsersConfig',







]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # cors 中间件
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 添加访问呢后端白名单
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'api_platform_beta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api_platform_beta.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
         # 指定引擎
        'ENGINE': 'django.db.backends.mysql',
        # 指定数据库名称
        'NAME': 'api_platform',
        # 数据库用户名
        'USER': 'root',
        # 数据库密码
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF配置信息
REST_FRAMEWORK = {

    # 修改配置只支持JSON
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    # 过滤引擎
    # 'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter'],
    # 指定分页引擎
    # 'DEFAULT_PAGINATION_CLASS': 'utils.pagenation.PageNumberPagination',
    # 'PAGE_SIZE': 3,
    # api 文档配置
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 指定认证方式
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # JWT 认证
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    # 认证权限
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

}

# jwt 配置
JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'utils.handle_jwt_response.jwt_response_payload_handler',
    # 指定token的有效期，默认为seconds=300
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 指定token前缀
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}
# 指定用户模型类 users.models.UsersModel， models不需要，指定为：users.UsersModel,自带的够用了，不需要改
AUTH_USER_MODEL = 'users.UsersModel'

# 指定存放用例文件的根路径
SUITE_DIR = os.path.join(BASE_DIR, 'suites')