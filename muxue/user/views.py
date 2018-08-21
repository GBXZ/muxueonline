from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login #用户认证方法；
from user import models
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.views.generic.base import View  #登陆View类，里面包含，get,post方法
from user.forms import LoginForm,RegisterForm,FindForm
from django.contrib.auth.hashers import make_password #对密码进行加密
from utils.email_send import send_register_email


class CustomBackend(ModelBackend):
	def authenticate(self,username=None,passowrod=None, **kwargs):
		try:
			user = models.UserProfile.objects.get(Q(username=username)|Q(email=username))
			if user.check_password(password):
				return user
		except Exception as e:
			return None 


 #登陆验证方法
class Login_view(View):         
	def get(self,request):
		login_form = LoginForm()
		return render(request,"user/login.html",locals())
	def post(self,request):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data["username"]
			password = login_form.cleaned_data["password"]
			user = authenticate(request,username=username,password=password) #如果认证成功，返回authenticate对象，如果失败返回None
			user_msg = models.UserProfile.objects.filter(username = username)
			for p_msg in user_msg:
				user_status = p_msg.is_active
			if user is not None:
				login(request, user)  #调用login,
				request.session["usrname"] = username
				return redirect("/user/index/")
			elif user_status == False:
				msg = "the account is invaliable"
				return render(request,"user/login.html",locals())
			else:
				msg = "帐号或者密码错误"
				return render(request,"user/login.html",locals())
		else:
			return render(request,"user/login.html",locals())

#注册页面
class Registerview(View):
	def get(self,request):
		register_form = RegisterForm()
		return render(request,"user/register.html",locals())
	def post(self,request):
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			useremail = register_form.cleaned_data["email"]
			password = register_form.cleaned_data["password"]
			if models.UserProfile.objects.filter(username=useremail):
				msg = "this account is already existed"
				return render(request,"user/register.html",locals())
			else:
				user_profile = models.UserProfile()
				user_profile.username = useremail
				user_profile.email = useremail
				user_profile.password = make_password(password)
				user_profile.is_active = False
				user_profile.save()
				send_register_email(useremail,send_type="register")
				return render(request,"user/login.html")
		else:
			return render(request,"user/register.html",locals())

#激活
def jihuo(request,nid):
	if models.EmailVerifyRecord.objects.filter(code=nid):
		email_code = models.EmailVerifyRecord.objects.filter(code=nid)
		for code_msg in email_code:
			email = code_msg.email
			usr_msg = models.UserProfile.objects.get(username = email)   #must using get,don't using filter
			usr_msg.is_active = True
			usr_msg.save()
			return render(request,"user/login.html")
	else:
		return HttpResponse("激活失败")
		
#find the password
class Find_password(View):
		def get(self,request):
			find_form = FindForm()
			return render(request,"user/forgetpwd.html",locals())
		def post(self,request):
			email = request.POST["email"]
			if models.UserProfile.objects.filter(username=email):
				find_form = FindForm(request.POST)
				if find_form.is_valid():			
					send_register_email(email,send_type="forget")
					request.session["email"]  = email
					return redirect("/user/reset/")
				else:
					msg = "captcha is error"
					return render(request,"user/forgetpwd.html",locals())
			else:
				msg = "the account is not exist"
				return render(request,"user/forgetpwd.html",locals())
			
			
			
#reset password
def reset_password(request,nid):
	if method == "GET":
		return render(request,"user/password_reset.html")
	if method == "POST":
		password = request.POST["password"]
		password2 = request.POST["passwprd2"]
		if password != password:
			msg = "Two passwords are inconsistent"
			return render(request,"user/password_reset.html",locals())
		else:
			email = request.session.get["email"]
			models.UserProFile.objects.filter(username = email).update(password = password2)
			return HttpResponse("OK")
			
			
def index(request):
	usrname = request.session.get("usrname")
	return render(request,"user/index.html",locals()) 	
# Create your views here.
