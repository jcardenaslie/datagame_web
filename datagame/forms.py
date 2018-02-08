from django.contrib.auth.models import User
from django import forms

from django.contrib.auth import authenticate, login,get_user_model, logout


User = get_user_model()


class UserForm(forms.ModelForm):
	
	password = forms.CharField(widget=forms.PasswordInput)
	
	#info about the class
	class Meta:
		model = User
		fields = ['username','email','password']
		widgets = {
			'myfield':forms.TextInput(attrs={'class':''})
		}


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")
			if not user.is_active:
				raise forms.ValidationError("This user is not longer active")
		
		return super(UserLoginForm,self).clean(*args, **kwargs)

