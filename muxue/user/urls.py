from django.urls import path,re_path
from user import views

urlpatterns = [
	path("login/",views.Login_view.as_view(),name="login"), #类转换为view方法
	path("index/",views.index,name="index"),
	path("register/",views.Registerview.as_view(),name="register"),
	path("find/",views.Find_password.as_view()),
	re_path("reset/(?P<nid>.{*})",views.reset_password),
	
]
# Create your tests here.
