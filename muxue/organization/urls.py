from django.urls import path,re_path
from organization import views

urlpatterns = [
	re_path("org_list/(?P<nid>\d*)",views.Org_list.as_view())
	
]
# Create your tests here.
