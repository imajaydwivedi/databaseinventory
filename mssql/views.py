from django.shortcuts import render
from . import models
from django.db.models import Q
from django.db import connection
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from databaseinventory.utils import dictfetchall
from django.urls import reverse, reverse_lazy


class IndexView(TemplateView):
    template_name = 'mssql/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['databaseinventory'] = models.databaseinventory
        context['servermaintenance'] = models.servermaintenance
        return context


def server(request):
    cursor = connection.cursor()
    try:
        cursor.execute("""
select  ServerID, ServerName, ApplicationId, 
        EnvironmentType, FQDN, IPAddress, Domain, 
        IsStandaloneServer, IsSqlClusterNode, IsAgNode, IsWSFC, 
        IsSqlCluster, IsAG, ParentServerId, OS, 
        SPVersion, IsVM, IsPhysical, Manufacturer, 
        Model, RAM, CPU, Powerplan, 
        OSArchitecture, ISDecom, DecomDate, GeneralDescription, 
        Remark1, Remark2, CollectionDate, CollectedBy, 
        UpdatedDate, UpdatedBy
from Server
""")
        # https://stackoverflow.com/a/14294314/4449743
        serverData = dictfetchall(cursor)
    # catch:
        #raise ValueError('Could not fetch data from INFORMATION_SCHEMA.COLUMNS')
    finally:
        cursor.close()

    servers = {'serverData': serverData}
    return render(request, 'mssql/server.html', context=servers)


def instance(request):
    cursor = connection.cursor()
    try:
        cursor.execute("""
SELECT	i.[InstanceID]
      ,s.ServerName
      ,i.[SqlInstance]
      ,i.[InstanceName]
      ,i.[RootDirectory]
      ,i.[Version]
      ,i.[CommonVersion]
      ,i.[Build]
      ,i.[VersionString]
      ,i.[Edition]
      ,i.[Collation]
      ,i.[ProductKey]
      ,i.[DefaultDataLocation]
      ,i.[DefaultLogLocation]
      ,i.[DefaultBackupLocation]
      ,i.[ErrorLogPath]
      ,i.[ServiceAccount]
      ,i.[Port]
      ,i.[IsStandaloneInstance]
      ,i.[IsSQLCluster]
      ,i.[IsAGListener]
      ,i.[IsAGNode]
      ,i.[AGListener]
      ,i.[HasOtherHASetup]
      ,i.[HARole]
      ,i.[HAPartner]
      ,i.[IsPowershellLinked]
      ,i.[IsDecom]
      ,i.[DecomDate]
      ,i.[CollectionDate]
      ,i.[CollectedBy]
      ,i.[UpdatedDate]
      ,i.[UpdatedBy]
      ,i.[Remark1]
      ,i.[Remark2]
FROM	Instance as i
INNER JOIN
		Server as s
	ON	s.ServerID = i.ServerID
WHERE   i.IsDecom = 0 or i.IsDecom IS NULL
        """)
        # https://stackoverflow.com/a/14294314/4449743
        instanceData = dictfetchall(cursor)
    # catch:
        #raise ValueError('Could not fetch data from INFORMATION_SCHEMA.COLUMNS')
    finally:
        cursor.close()

    instances = {'instanceData': instanceData}
    return render(request, 'mssql/instance.html', context=instances)


class ApplicationListView(ListView):
    context_object_name = 'applications'
    model = models.Application

class ApplicationDetailView(DetailView):
    context_object_name = 'application_detail'
    model = models.Application
    
    template_name = 'mssql/application_detail.html'

class ApplicationCreateView(CreateView):
    model = models.Application
    fields = ['category','businessunit','applicationname','priority','businessowner','technicalowner','secondarytechnicalowner','remark1','remark2']

class ApplicationUpdateView(UpdateView):
    model = models.Application
    fields = ['category','businessunit','applicationname','priority','businessowner','technicalowner','secondarytechnicalowner','remark1','remark2']

class ApplicationDeleteView(DeleteView):
    model = models.Application
    success_url = reverse_lazy("mssql:application")


class ServerListView(ListView):
    context_object_name = 'servers'
    model = models.Server

    def get_queryset(self):
        # https://docs.djangoproject.com/en/2.1/ref/models/querysets/#select-related
        # return models.Server.objects.select_related('applicationid').filter(Q(isdecom=0) | Q(isdecom=None))
        return models.Server.objects.prefetch_related('applicationid').filter(Q(isdecom=0) | Q(isdecom=None))

class ServerDetailView(DetailView):
    context_object_name = 'server_detail'
    model = models.Server
    
    template_name = 'mssql/server_detail.html'

class ServerCreateView(CreateView):
    model = models.Server
    fields = ['servername','applicationid','environmenttype','fqdn','ipaddress','domain','isstandaloneserver','issqlclusternode','isagnode','iswsfc','issqlcluster','isag','parentserverid','os','spversion','isvm','isphysical','manufacturer','model','ram','cpu','powerplan','osarchitecture','generaldescription','remark1','remark2']

class ServerUpdateView(UpdateView):
    model = models.Server
    fields = ['servername','applicationid','environmenttype','fqdn','ipaddress','domain','isstandaloneserver','issqlclusternode','isagnode','iswsfc','issqlcluster','isag','parentserverid','os','spversion','isvm','isphysical','manufacturer','model','ram','cpu','powerplan','osarchitecture','isdecom','decomdate','generaldescription','remark1','remark2']

class ServerDeleteView(DeleteView):
    model = models.Server
    success_url = reverse_lazy("mssql:server")


class InstanceListView(ListView):
    context_object_name = 'instances'
    model = models.Instance

    def get_queryset(self):
        return models.Instance.objects.prefetch_related('serverid','aglistener','hapartner').filter(Q(isdecom=0) | Q(isdecom=None))

class InstanceDetailView(DetailView):
    context_object_name = 'instance_detail'
    model = models.Instance
    
    template_name = 'mssql/instance_detail.html'

class InstanceCreateView(CreateView):
    model = models.Instance
    fields = ['serverid','sqlinstance','instancename','rootdirectory','version','commonversion','build','versionstring','edition','collation','productkey','defaultdatalocation','defaultloglocation','defaultbackuplocation','errorlogpath','serviceaccount','port','isstandaloneinstance','issqlcluster','isaglistener','isagnode','aglistener','hasotherhasetup','harole','hapartner','ispowershelllinked','remark1','remark2']

class InstanceUpdateView(UpdateView):
    model = models.Instance
    fields = ['serverid','sqlinstance','instancename','rootdirectory','version','commonversion','build','versionstring','edition','collation','productkey','defaultdatalocation','defaultloglocation','defaultbackuplocation','errorlogpath','serviceaccount','port','isstandaloneinstance','issqlcluster','isaglistener','isagnode','aglistener','hasotherhasetup','harole','hapartner','ispowershelllinked','isdecom','decomdate','remark1','remark2']

class InstanceDeleteView(DeleteView):
    model = models.Instance
    success_url = reverse_lazy("mssql:instance")



class DatabaseListView(ListView):
    context_object_name = 'databases'
    model = models.Database

    def get_queryset(self):
        return models.Database.objects.prefetch_related('instanceid')

class DatabaseDetailView(DetailView):
    context_object_name = 'database_detail'
    model = models.Database
    
    template_name = 'mssql/database_detail.html'

class DatabaseCreateView(CreateView):
    model = models.Database
    fields = ['instanceid','databasename','createddate','recoverymodel','currentdbsize','backuppath']

class DatabaseUpdateView(UpdateView):
    model = models.Database
    fields = ['instanceid','databasename','createddate','recoverymodel','currentdbsize','backuppath']

class DatabaseDeleteView(DeleteView):
    model = models.Database
    success_url = reverse_lazy("mssql:database")



class BackupscheduleListView(ListView):
    context_object_name = 'backupschedules'
    model = models.Backupschedule

    def get_queryset(self):
        return models.Backupschedule.objects.prefetch_related('instanceid')

class BackupscheduleDetailView(DetailView):
    context_object_name = 'backupschedule_detail'
    model = models.Backupschedule
    
    template_name = 'mssql/backupschedule_detail.html'

class BackupscheduleCreateView(CreateView):
    model = models.Backupschedule
    fields = ['instanceid','timefrom','timeto']

class BackupscheduleUpdateView(UpdateView):
    model = models.Backupschedule
    fields = ['instanceid','timefrom','timeto']

class BackupscheduleDeleteView(DeleteView):
    model = models.Backupschedule
    success_url = reverse_lazy("mssql:backupschedule")


class CommandqueueListView(ListView):
    context_object_name = 'commandqueues'
    model = models.Commandqueue

    def get_queryset(self):
        return models.Commandqueue.objects.prefetch_related('instanceid','databaseid')

class CommandqueueDetailView(DetailView):
    context_object_name = 'commandqueue_detail'
    model = models.Commandqueue
    
    template_name = 'mssql/commandqueue_detail.html'

class CommandqueueCreateView(CreateView):
    model = models.Commandqueue
    fields = ['instanceid','databaseid','command','jobid','jobtype','status','reason','priority']

class CommandqueueUpdateView(UpdateView):
    model = models.Commandqueue
    fields = ['instanceid','databaseid','command','jobid','jobtype','status','reason','priority']

class CommandqueueDeleteView(DeleteView):
    model = models.Commandqueue
    success_url = reverse_lazy("mssql:commandqueue")



class LoggingListView(ListView):
    context_object_name = 'loggings'
    model = models.Logging

class LoggingDetailView(DetailView):
    context_object_name = 'logging_detail'
    model = models.Logging
    
    template_name = 'mssql/logging_detail.html'

class LoggingCreateView(CreateView):
    model = models.Logging
    fields = ['logid','logmessage']

class LoggingUpdateView(UpdateView):
    model = models.Logging
    fields = ['logid','logmessage']

class LoggingDeleteView(DeleteView):
    model = models.Logging
    success_url = reverse_lazy("mssql:logging")


class BackuphistoryListView(ListView):
    context_object_name = 'backuphistories'
    model = models.Backuphistory

    def get_queryset(self):
        return models.Backuphistory.objects.prefetch_related('instanceid','databaseid')

class BackuphistoryDetailView(DetailView):
    context_object_name = 'backuphistory_detail'
    model = models.Backuphistory
    
    template_name = 'mssql/backuphistory_detail.html'
