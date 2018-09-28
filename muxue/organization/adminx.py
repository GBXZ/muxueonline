from django.contrib import admin
from organization.models import CityDict,CourseOrg,Teacher
import xadmin

class CityDictAdmin(object):
	list_display = ["name","decs","add_time"]
	search_fields = ["name","decs"]
	list_filter = ["name","decs","add_time"]


class CourseOrgAdmin(object):
	list_display = ["name","desc","click_nums","fav_nums","imge","address","city","add_time","students","course_nums"]
	search_fields = ["name","desc","click_nums","fav_nums","imge","address","city","students","course_nums"]
	list_filter = ["name","desc","click_nums","fav_nums","imge","address","city","add_time","students","course_nums"]

class TeacherAdmin(object):
	list_display = ["org","name","work_years","work_company","work_position","points","click_nums","fav_nums","add_time"]
	search_fields = ["org","name","work_years","work_company","work_position","points","click_nums","fav_nums"]
	list_filter = ["org","name","work_years","work_company","work_position","points","click_nums","fav_nums","add_time"]

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
# Register your models here.
