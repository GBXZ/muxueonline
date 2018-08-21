from django import forms
from  captcha.fields import CaptchaField


class LoginForm(forms.Form):
	username = forms.CharField(required=True,max_length = 20)
	password = forms.CharField(required=True,max_length = 20,min_length=5)


class RegisterForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True,min_length=5)
	captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

class FindForm(forms.Form):
		captcha =CaptchaField(error_messages={"invalid":"captcha is error"})