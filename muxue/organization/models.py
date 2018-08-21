# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models

class CityDict(models.Model):
	name = models.CharField(max_length=20,verbose_name = u"城市")
	decs = models.CharField(max_length=200,verbose_name = u"城市描述")
	add_time = models.DateTimeField(default= datetime.now)
	class Meta:
		verbose_name = u"城市"
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.name

class CourseOrg(models.Model):
	name = models.CharField(max_length=50,verbose_name=u"机构名称")
	desc = models.TextField(verbose_name = u"机构描述")
	click_nums = models.IntegerField(verbose_name = u"点击数")
	fav_nums = models.IntegerField(default = 0,verbose_name =u"收藏数")
	imge = models.ImageField(upload_to="org/%Y/%m",verbose_name = u"封面图",max_length = "100")
	address = models.CharField(max_length=150,verbose_name=u"机构地址")
	city = models.ForeignKey(CityDict,on_delete=models.CASCADE,verbose_name=u"所在城市")
	add_time = models.DateTimeField(default= datetime.now)
	class Meta:
		verbose_name = u"课程机构"
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.name

class Teacher(models.Model):
	org =models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name = u"所属机构")
	name = models.CharField(max_length=50,verbose_name = u"教师名字")
	work_years = models.IntegerField(verbose_name = u"工作年限")
	work_company = models.CharField(max_length=50,verbose_name=u"工作公司")
	work_position = models.CharField(max_length=50,verbose_name = "工作职位")
	points = models.CharField(max_length = 50,verbose_name = u"教学特点")
	click_nums = models.IntegerField(verbose_name = u"点击数")
	fav_nums = models.IntegerField(default = 0,verbose_name =u"收藏数")
	add_time = models.DateTimeField(default= datetime.now)
	class Meta:
		verbose_name = u"课程教师"
		verbose_name_plural = verbose_name
# Create your models here.
