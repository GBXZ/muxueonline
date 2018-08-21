# _*_ coding:utf-8 _*_

from django.contrib import admin
from .models import EmailVerifyRecord,Banner
from django.db import models
from datetime import datetime
import xadmin  #重要
from xadmin import views   #修改主题需要导入views


class BaseSetting(object):  #修改xadmin主题
	enable_themes = True
	use_bootswatch = True

class GlobalSettings(object):  #修改xadmin头部和底部字体
	site_title = "慕学后台管理系统"
	site_footer = "慕学在线网"
	menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
	list_display = ["code","email","send_type","send_time"]  #显示的字段
	search_fields = ["code","email","send_type"] #能够搜索的字段
	list_filter = ["code","email","send_type","send_time"]  #过滤器


class BannerAdmin(object):
	list_display = ["title","image","url","index","add_time"]  #显示的字段
	search_fields = ["title","image","url","index"] #能够搜索的字段
	list_filter = ["title","image","url","index","add_time"] #过滤器


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)  #用来修改xadmin主题
xadmin.site.register(views.CommAdminView,GlobalSettings) #用来修改xadmin底部头部字体
# Register your models here.

