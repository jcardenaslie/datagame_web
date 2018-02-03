from django.urls import path

from . import views



app_name = 'datagame'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
]