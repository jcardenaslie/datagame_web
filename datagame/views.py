from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login,get_user_model, logout
from django.views.generic import View
from .forms import UserForm, UserLoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
	print(request.user.is_authenticated)
	title = "Login"
	form = UserLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request,user)
		print(request.user.is_authenticated)
		return redirect('../search')

		# return redirect('datagame:search')

	# return render(request,"datagame/form.html", {'form':form, 'title':title})
	return render(request,"home/index.html", {'form':form})


@login_required(login_url='../login/')
def search(request):
	return HttpResponse("Hello you are at the main page")


class UserFormView(View):
	form_class = UserForm
	template_name = 'datagame/registration_form.html'

	#displays a blank form
	def get(self,request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	# process form data
	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#return User object if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('datagame:search')

		return render(request, self.template_name, {'form':form})


def login_view(request):
	print(request.user.is_authenticated)

	title = "Login"
	form = UserLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request,user)
		print(request.user.is_authenticated)
		return redirect('../search')

		# return redirect('datagame:search')

	# return render(request,"datagame/form.html", {'form':form, 'title':title})
	return render(request,"datagame/form.html", {'form':form, 'title':title})


def register_view(request):
	return render(request,'form,html', {})


def logout_view(request):
	logout(request)
	return redirect('..')