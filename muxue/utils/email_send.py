from random import Random


from django.shortcuts import render,HttpResponse
from user.models import EmailVerifyRecord
from django.core.mail import send_mail
from muxue.settings import EMAIL_FROM
from user import models


def random_str(randomlength=8):
	str = ""
	chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVüWwXxYyZz0123456789"
	length=len(chars)-1
	random = Random()
	for i in range(randomlength):
		str+=chars[random.randint(0,length)]
	return str
	

def send_register_email(email,send_type):
	email_record = EmailVerifyRecord()
	code = random_str(16)
	email_record.code = code
	email_record.email = email
	email_record.send_type =  send_type
	email_record.save()
	email_title = ""
	email_body = ""
	if send_type == "register":
		email_title = "慕学在线网注册激活链接"
		email_body = "请点击下面链接激活您的帐号：http://127.0.0.1:8000/active/{0}".format(code)			
		send_mail(email_title,email_body,EMAIL_FROM,[email])
	if send_type == "forget":
		usr_msg = models.UserProfile.objects.filter(username=email)
		for usr in usr_msg:
				pwd = usr.password
		email_title = "慕学在线网注册激活链接"
		email_body = "http://127.0.0.1:8000/user/reset/{0}".format(code)	
		send_mail(email_title,email_body,EMAIL_FROM,[email])
		
