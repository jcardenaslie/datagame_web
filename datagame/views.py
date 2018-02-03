from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
# Create your views here.

def index(request):
    return render(
        request,
        'home/index.html',
        # context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

def home(request):
	return HttpResponse("Hello you are at the main page")


# class HomeView(View):
# 	def get(self, request, *args, **kwargs):
# 		return render(request, "datagame/index.html", {})