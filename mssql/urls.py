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
    # dbo.Application
    path('application/',views.ApplicationListView.as_view(),name='application'),
    path('application/<int:pk>/', views.ApplicationDetailView.as_view(),name='applicationdetail'),
    path('application/create/', views.ApplicationCreateView.as_view(), name='applicationcreate'),
    path('application/update/<int:pk>/', views.ApplicationUpdateView.as_view(), name='applicationupdate'),
    path('application/delete/<int:pk>/', views.ApplicationDeleteView .as_view(), name='applicationdelete'),
    # dbo.Server
    # path('server/',views.server,name='server'),
    path('server/',views.ServerListView.as_view(),name='server'),
    path('server/<int:pk>/', views.ServerDetailView.as_view(),name='serverdetail'),
    path('server/create/', views.ServerCreateView.as_view(), name='servercreate'),
    path('server/update/<int:pk>/', views.ServerUpdateView.as_view(), name='serverupdate'),
    path('server/delete/<int:pk>/', views.ServerDeleteView .as_view(), name='serverdelete'),
    # dbo.Instance
    path('instance/', views.InstanceListView.as_view(), name='instance'),
    path('instance/<int:pk>/', views.InstanceDetailView.as_view(),name='instancedetail'),
    path('instance/create/', views.InstanceCreateView.as_view(), name='instancecreate'),
    path('instance/update/<int:pk>/', views.InstanceUpdateView.as_view(), name='instanceupdate'),
    path('instance/delete/<int:pk>/', views.InstanceDeleteView .as_view(), name='instancedelete'),
    # dbo.Databases
    path('database/', views.DatabaseListView.as_view(), name='database'),
    path('database/<int:pk>/', views.DatabaseDetailView.as_view(),name='databasedetail'),
    path('database/create/', views.DatabaseCreateView.as_view(), name='databasecreate'),
    path('database/update/<int:pk>/', views.DatabaseUpdateView.as_view(), name='databaseupdate'),
    path('database/delete/<int:pk>/', views.DatabaseDeleteView .as_view(), name='databasedelete'),
    # dbo.Backupschedule
    path('backupschedule/',views.BackupscheduleListView.as_view(),name='backupschedule'),
    path('backupschedule/<int:pk>/', views.BackupscheduleDetailView.as_view(),name='backupscheduledetail'),
    path('backupschedule/create/', views.BackupscheduleCreateView.as_view(), name='backupschedulecreate'),
    path('backupschedule/update/<int:pk>/', views.BackupscheduleUpdateView.as_view(), name='backupscheduleupdate'),
    path('backupschedule/delete/<int:pk>/', views.BackupscheduleDeleteView .as_view(), name='backupscheduledelete'),
    # dbo.Commandqueue
    path('commandqueue/',views.CommandqueueListView.as_view(),name='commandqueue'),
    path('commandqueue/<int:pk>/', views.CommandqueueDetailView.as_view(),name='commandqueuedetail'),
    path('commandqueue/create/', views.CommandqueueCreateView.as_view(), name='commandqueuecreate'),
    path('commandqueue/update/<int:pk>/', views.CommandqueueUpdateView.as_view(), name='commandqueueupdate'),
    path('commandqueue/delete/<int:pk>/', views.CommandqueueDeleteView .as_view(), name='commandqueuedelete'),
    # dbo.Logging
    path('logging/', views.LoggingListView.as_view(), name='logging'),
    path('logging/<int:pk>/', views.LoggingDetailView.as_view(),name='loggingdetail'),
    path('logging/create/', views.LoggingCreateView.as_view(), name='loggingcreate'),
    path('logging/update/<int:pk>/', views.LoggingUpdateView.as_view(), name='loggingupdate'),
    path('logging/delete/<int:pk>/', views.LoggingDeleteView .as_view(), name='loggingdelete'),
    # dbo.Backuphistory
    path('backuphistory/', views.BackuphistoryListView.as_view(), name='backuphistory'),
    path('backuphistory/<int:pk>/', views.BackuphistoryDetailView.as_view(),name='backuphistorydetail'),
]
