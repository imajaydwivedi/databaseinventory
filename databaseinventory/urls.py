"""databaseinventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from users import views as usr_views
from mssql import views as tsql_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    url(r'^mssql/', include('mssql.urls',namespace='mssql'), name='mssql'),
    url(r'^users/', include('users.urls',namespace='users'), name='users'),
    url(r'^logout/$', usr_views.user_logout, name = 'logout'),
]

admin.site.site_header = 'DbInventory administration'