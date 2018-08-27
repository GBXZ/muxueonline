"""
Django settings for muxue project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*=1%d1*8+v4=127+_%9r(^lh46-g0hk$w7&^huxv2#opxqw%%$'

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
      'user',
	'course',
	'organization',
	'operation',
	'xadmin', 
	'crispy_forms', #配置xadmin必须使用
	'captcha',
]

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge' #captcha验证码类型换为数字加减乘除


AUTH_USER_MODEL = "user.UserProfile"  #因为重写了django原有的用户类，所以要在settings里面重载方法，app名称加重写的类

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'muxue.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
		   'django.template.context_processors.media', #
            ],
        },
    },
]

WSGI_APPLICATION = 'muxue.wsgi.application'

AuTHENTICATION_BACKENDS = ("user.views.CustomBackend",) #自定义验证字段
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'muxue',
	  'USER':'root',
	'PASSWORD':'welovezxy',
	'HOST':'localhost',
	'PORT':'3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False #如果为True存储数据的时间为UTC，应该改为False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static"),
	os.path.join(BASE_DIR,"/orgaization/static/"),
	os.path.join(BASE_DIR,"/user/static/"),
]

'''
上传文件设置，url是路径，root是上传的存放点
'''
MEDIA_URL = '/media/'  
MEDIA_ROOT = os.path.join(BASE_DIR,"media")


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.163.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "hupan0818@163.com"
EMAIL_HOST_PASSWORD = "slh368601"
EMAIL_FROM = EMAIL_HOST_USER
EMAIL_USE_TLS = True

