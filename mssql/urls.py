# from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url
from mssql import views

# TEMPLATE URLS!
app_name = 'mssql'


# https://docs.djangoproject.com/en/2.1/ref/urls/
# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('server/',views.ServerListView.as_view(),name='server'),
    path('server/<int:pk>/', views.ServerDetailView.as_view(),name='serverdetail'),
    path('server/create/', views.ServerCreateView.as_view(), name='servercreate'),
    path('server/update/<int:pk>/', views.ServerUpdateView.as_view(), name='serverupdate'),
    path('server/delete/<int:pk>/', views.ServerDeleteView .as_view(), name='serverdelete'),
    path('instance/', views.instance, name='instance'),
]
