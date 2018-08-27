#_*_encoding:utf-8_*_


from django.shortcuts import render
from django.views.generic.base import View
from .models import CourseOrg,CityDict

class Org_list(View):
	"""
	课程机构列表功能
	"""
	def get(self,request):
		#取出课程机构
		all_orgs = CourseOrg.objects.all()
		#取出城市地址
		all_citys = CityDict.objects.all()
		return render(request,"organization/org-list.html",{"all_orgs":all_orgs,"all_citys":all_citys})

# Create your views here.
