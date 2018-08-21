# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):   #用户信息设计，继承django原有的用户类
	nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default ="")
	birthday =models.DateField(verbose_name=u"生日",null=True)
	gender = models.CharField(choices=(("male","男"),("female","女")),default="female",max_length=10)
	address = models.CharField(max_length=100,default="")
	mobile = models.CharField(max_length = 11,null=True,blank=True)
	image = models.ImageField(upload_to="imgae/%Y/%m",default=u"imge/default.png",max_length = 100)
	class Meta:
		verbose_name = "用户信息"
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.username


class EmailVerifyRecord(models.Model):  #验证码设计
	code = models.CharField(max_length=20,verbose_name=u"验证码")
	email = models.CharField(max_length=50,verbose_name=u"邮箱")
	send_type = models.CharField(choices=(("register","注册"),("forget","忘记密码")),max_length=10)
	send_time = models.DateTimeField(default=datetime.now)
	class Meta:
		verbose_name = u"邮箱验证码"
		verbose_name_plural = verbose_name


class Banner(models.Model):   #纶播图设计
	title = models.CharField(max_length=100,verbose_name=u"标题")
	image = models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图")
	url =models.URLField(max_length=200,verbose_name=u"访问地址")
	index = models.IntegerField(default=100,verbose_name=u"顺序")
	add_time = models.DateTimeField(default = datetime.now,verbose_name = u"添加时间")
	class Meta:
		verbose_name = u"轮播图"
		verbose_name_plural = verbose_name
