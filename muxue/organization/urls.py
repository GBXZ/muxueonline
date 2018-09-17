from django.urls import path,re_path
from organization import views

urlpatterns = [
	re_path("^org_list/(?P<nid>\d*)$",views.Org_list.as_view()),
	re_path("org_list/(?P<uid>[a-z]+)/(?P<nid>\d*)",views.Org_by_city.as_view()),
	
]
# Create your tests here.
