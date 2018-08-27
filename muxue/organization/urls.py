from django.urls import path,re_path
from organization import views

urlpatterns = [
	path("org_list/",views.Org_list.as_view())
	
]
# Create your tests here.
