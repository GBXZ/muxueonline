#_*_ encoding:utf-8 _*_

from django.forms import ModelForm
from operation.models import UserAsk

class UserAskForm(ModelForm):
	
	class Meta:
		models = UserAsk
		fields = ['name','mobile','course_name']
