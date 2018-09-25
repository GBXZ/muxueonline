#_*_encoding:utf-8_*_


from django.shortcuts import render,HttpResponse
from django.views.generic.base import View
from .models import CourseOrg,CityDict
from django.core.paginator import Paginator
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger #使用pure-pagination需要导入的模块

class Org_list(View):
	"""
	课程机构列表功能
	"""
	def get(self,request,nid):
		#取出课程机构
		all_orgs = CourseOrg.objects.all().order_by("id")  #对数据进行排序，否则分页会报错，
		#通过城市筛选出课程机构，前端 <a href="?city={{city.id}}"><span class="">{{city.name}}</span></a>，用request.GET.get得到city，因为得到的city有一个/，所以使用strip祛除
		city_id = request.GET.get('city',"").strip('/')
		if city_id:
			all_orgs = CourseOrg.objects.filter(city_id = int(city_id)).order_by('id')
		#通过机构类别筛选出课程机构
		org_category = request.GET.get('ct',"").strip('/')
		if org_category:
			all_orgs = CourseOrg.objects.filter(category = org_category).order_by('id')	
		#取出城市地址
		orgs_total = len(all_orgs)
		all_citys = CityDict.objects.all()
		'''
		paginator = Paginator(all_orgs,5)  #将取出数据每5条分为 一页
		yeshu = paginator.page_range    #得到页码的一个range列表
		if nid == "":
			nid = 1
		page = paginator.page(nid)  #展示每页数据
		#下一页,默认下一页等于当前页+1，如果当前页为最大页，下一页就为当前页
		xia = int(nid) + 1
		if xia>paginator.num_pages:  
			xia = paginator.num_pages
		'''
		#使用pure-pagination进行分页
		try:
			page = request.GET.get('page',1)
		except PageNotAnteger:
			page = 1
		p = Paginator(all_orgs,2,request=request)
		orgs =  p.page(page)
		return render(request,"organization/org-list.html",locals())
#通过地市筛选出课程机构
class Org_by_city(View):
	def get(self,request,uid,nid):
		#此段代码是用来得到城市的课程机构，首先通过url中uid查询到对应的query_set,然后再遍历出id，然后通过课程外键，得到所有课程机构
		citys = CityDict.objects.filter(pinyin_name = uid)
		for city in citys:
			city_id = city.id
			#创建一个变量名，变量名指向uid对象，要将该对象传递到前端目标，分页url需要用到
			city_pinyin_name = city.pinyin_name
		all_orgs = CourseOrg.objects.filter(city=city_id).order_by('id')
		#计算出该地市有多少培训机构
		orgs_total = len(all_orgs)
		#得到所有城市
		all_citys = CityDict.objects.all()
		#进行分页
		paginator = Paginator(all_orgs,5)
		yeshu = paginator.page_range
		if nid == "":
			nid = 1
		page = paginator.page(nid)
		xia = int(nid) + 1
		if xia > paginator.num_pages:
			xia = paginator.num_pages
		return render(request,"organization/org-list_order_by_city.html",locals())
		
# Create your views here.
