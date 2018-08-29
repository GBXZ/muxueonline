#_*_encoding:utf-8_*_


from django.shortcuts import render
from django.views.generic.base import View
from .models import CourseOrg,CityDict
from django.core.paginator import Paginator


class Org_list(View):
	"""
	课程机构列表功能
	"""
	def get(self,request,nid):
		#取出课程机构
		all_orgs = CourseOrg.objects.all().order_by("id")  #对数据进行排序，否则分页会报错，
		#取出城市地址
		orgs_total = len(all_orgs)
		all_citys = CityDict.objects.all()
		paginator = Paginator(all_orgs,5)  #将取出数据每5条分为一页
		yeshu = paginator.page_range    #得到页码的一个range列表
		if nid == "":
			nid = 1
		page = paginator.page(nid)  #展示每页数据
		return render(request,"organization/org-list.html",locals())

# Create your views here.
