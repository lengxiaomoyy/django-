"""
Django settings for day06 project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

import pymysql as pymysql

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s!haoke$ig#dbkfyl4p__$di%2mx(y-eyf@h)9u2oc3zv97)3)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "web.apps.WebConfig"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.md.AuthMiddleware'
]

ROOT_URLCONF = 'day06.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'day06.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'day06',
        'USER': 'root',
        'PASSWORD': '28658488',
        'HOST': 'localhost',  # 或者数据库的主机地址
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
        'CONN_MAX_AGE': 600,
        # 可选：数据库的端口号
    }
}
pymysql.install_as_MySQLdb()
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
# session配置

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',  # Redis 服务器地址
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    # 信息保持
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Redis 服务器地址
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    # 验证吗
    "verity_code": {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',  # Redis 服务器地址
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'session'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MENU = {
    "ADMIN": [],
    "CUSTOMER": [],
}
PERMISSION = {
    "ADMIN": {},
    "CUSTOMER": {},
}

# cache缓存



# ###################### 自定义配置 ######################
LOGIN_HOME = "/home/"
NB_SESSION_KEY = "user_info"
NB_LOGIN_URL = "/login/"
NB_WHITE_URL = ['/login/', '/sms/login/', '/sms/send/']

NB_MENU = {
    'ADMIN': [
        {
            'text': "用户信息",
            'icon': "fa-bed",
            'children': [
                {'text': "级别管理", 'url': "/level/list/", 'name': "level_list"},
                {'text': "客户管理", 'url': "/customer/list/", 'name': "customer_list"},
                {'text': "价格策略", 'url': "/policy/list/", 'name': "policy_list"},
            ]
        },
        {
            'text': "交易管理",
            'icon': "fa-bed",
            'children': [
                {'text': "交易记录", 'url': "/transaction/list/", 'name': "transaction_list"},
            ]
        },

    ],
    'CUSTOMER': [
        {
            'text': "订单中心",
            'icon': "fa-bed",
            'children': [
                {'text': "订单管理", 'url': "/my/order/list/", 'name': "my_order_list"},
                {'text': "我的交易记录", 'url': "/my/transaction/list/", 'name': "my_transaction_list"},
            ]
        },
    ],
}
NB_PERMISSION_PUBLIC = {
    "home": {"text": "主页", 'parent': None},
    "logout": {"text": "注销", 'parent': None},
}
NB_PERMISSION = {
    "ADMIN": {
        "level_list": {"text": "级别列表", 'parent': None},
        "level_add": {"text": "新建级别", 'parent': 'level_list'},
        "level_edit": {"text": "编辑级别", 'parent': 'level_list'},
        "level_delete": {"text": "删除级别", 'parent': 'level_list'},

        "customer_list": {"text": "客户列表", 'parent': None},
        "customer_add": {"text": "新建客户", 'parent': 'customer_list'},
        "customer_edit": {"text": "编辑客户", 'parent': 'customer_list'},
        "customer_delete": {"text": "删除客户", 'parent': 'customer_list'},
        "customer_reset": {"text": "重置密码", 'parent': 'customer_list'},
        "customer_charge": {"text": "我的交易记录", 'parent': 'customer_list'},
        "customer_charge_add": {"text": "创建交易记录", 'parent': 'customer_list'},

        "policy_list": {"text": "价格策略", 'parent': None},
        "policy_add": {"text": "创建价格策略", 'parent': 'policy_list'},
        "policy_edit": {"text": "编辑价格策略", 'parent': 'policy_list'},
        "policy_delete": {"text": "删除价格策略", 'parent': 'policy_list'},

        "transaction_list": {'text': "交易记录", 'name': "transaction_list", 'parent': None},

    },
    "CUSTOMER": {
        "my_order_list": {"text": "订单列表", 'parent': None},
        "my_order_add": {"text": "订单列表", 'parent': 'my_order_list'},
        "my_order_cancel": {"text": "订单列表", 'parent': 'my_order_list'},
        "my_transaction_list": {"text": "我的交易记录", 'parent': None},
    }
}

QUEUE_TASK_NAME = "YANG_TASK_QUEUE"

# 第4个位置
# MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
# MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MESSAGE_DANDER_TAG = 50
MESSAGE_TAGS = {
    MESSAGE_DANDER_TAG: "danger"
}


try:
    from .local_settings import *
except Exception:
    pass