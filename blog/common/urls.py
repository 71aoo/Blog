from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [

    path('', views.index, name='index'),
    path('index', views.index),
    path('friends', views.friends, name='friends'),
    path('archive', views.archive, name='archive'),
    path('about', views.about, name='about'),

]