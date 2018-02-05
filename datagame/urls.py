from django.urls import path

from . import views



app_name = 'datagame'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('search/', views.search, name='index'),
    # path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]