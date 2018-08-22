from django.urls import path,re_path
from user import views

urlpatterns = [
	path("login/",views.Login_view.as_view(),name="login"), #类转换为view方法
	path("index/",views.Index.as_view(),name="index"),
	path("register/",views.Registerview.as_view(),name="register"),
	path("find/",views.Find_password.as_view()),
	re_path("reset/(?P<nid>.{16})",views.reset_password),
	
]
# Create your tests here.
