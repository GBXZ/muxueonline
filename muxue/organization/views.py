#_*_encoding:utf-8_*_


from django.shortcuts import render,HttpResponse
from django.views.generic.base import View
from .models import CourseOrg,CityDict
from django.core.paginator import Paginator
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger #使用pure-pagination需要导入的模块
from .forms import UserAskForm


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

		#通过机构类别筛选出课程机构,request.GET.get('ct',"") 和request.GET['ct']一样，不过后者如果没参数，就会报错
		org_category = request.GET.get('ct',"").strip('/')
		if org_category:
			all_orgs = CourseOrg.objects.filter(category = org_category).order_by('id')

		#存在多个条件，多条件查询方式
		if city_id and org_category:
			all_orgs = CourseOrg.objects.filter(city_id = int(city_id),category = org_category).order_by('id')	

		#授课机构排名,取出前面三个用[:3]
		hot_orgs = CourseOrg.objects.all().order_by('-click_nums')[:3]
		
		#进行学习人数排序
		paixu = request.GET.get('sort','').strip('/')
		if paixu == 'students':
			all_orgs = CourseOrg.objects.all().order_by('-students')
		if paixu == 'students' and city_id:
			all_orgs = CourseOrg.objects.filter(city_id = int(city_id)).order_by('-students')
		if paixu == 'students' and org_category:
			all_orgs = CourseOrg.objects.filter(category = org_category).order_by('-students')
		if paixu == 'students' and org_category and city_id :
			all_orgs = CourseOrg.objects.filter(city_id = int(city_id),category = org_category).order_by('-students')
		#课程数排序
		if paixu == 'courses':
			all_orgs = CourseOrg.objects.all().order_by('-course_nums')
		if paixu == 'courses' and city_id:
			all_orgs = CourseOrg.objects.filter(city_id=int(city_id)).order_by('-course_nums')
		if paixu == 'courses' and org_category:
			all_orgs = CourseOrg.objects.filter(category = org_category).order_by('-course_nums')
		if paixu == 'courses' and org_category and city_id :
			all_orgs = CourseOrg.objects.filter(city_id = int(city_id),category = org_category).order_by('-course_nums')
								
		
		#得到课程个数
		orgs_total = len(all_orgs)

		#取出城市地址
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
		p = Paginator(all_orgs,5,request=request)
		orgs =  p.page(page)
		return render(request,"organization/org-list.html",locals())


class AddUserAsk(View):
	'''
	用户添加请求
	'''
	def post(self,request):
		UserAskForm = UserAskForm(request.POST)
		if UserAskForm.is_valid():
			user_ask = userask_form.save(commit=True) #commit=True直接把form字段存储到数据库
			return HttpResponse("{'status':'success'}",conent_type='application/json')
		else:
			return HttpResponse("{'status':'fail','msg':'登陆失败'}",content_type='application/json')		
			
# Create your views here.
