from django.urls import path
from django.conf.urls import url

from . import views



app_name = 'datagame'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url('search/', views.search, name='index'),
    url('login/', views.login_view, name='login'),
    url('logout/', views.logout_view, name='logout'),
]