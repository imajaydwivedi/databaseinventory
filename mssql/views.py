from django.shortcuts import render
from . import models
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
        return context


def server(request):
    cursor = connection.cursor()
    try:
        cursor.execute("select * from Server")
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
      ,i.[AGListenerName]
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
        """)
        # https://stackoverflow.com/a/14294314/4449743
        instanceData = dictfetchall(cursor)
    # catch:
        #raise ValueError('Could not fetch data from INFORMATION_SCHEMA.COLUMNS')
    finally:
        cursor.close()

    instances = {'instanceData': instanceData}
    return render(request, 'mssql/instance.html', context=instances)


class ServerListView(ListView):
    context_object_name = 'servers'
    model = models.Server
    # template_name = 'mssql/server_list.html'


class ServerDetailView(DetailView):
    context_object_name = 'server_detail'
    model = models.Server
    
    template_name = 'mssql/server_detail.html'


class ServerCreateView(CreateView):
    model = models.Server
    fields = ['servername','applicationid','environmenttype','fqdn','ipaddress','domain','isstandaloneserver','issqlclusternode','isagnode','iswsfc','issqlcluster','isag','parentserverid','os','spversion','isvm','isphysical','manufacturer','model','ram','cpu','powerplan','osarchitecture','generaldescription']


class ServerUpdateView(UpdateView):
    model = models.Server
    fields = ['servername','applicationid','environmenttype','fqdn','ipaddress','domain','isstandaloneserver','issqlclusternode','isagnode','iswsfc','issqlcluster','isag','parentserverid','os','spversion','isvm','isphysical','manufacturer','model','ram','cpu','powerplan','osarchitecture','isdecom','decomdate','generaldescription']


class ServerDeleteView(DeleteView):
    model = models.Server
    success_url = reverse_lazy("mssql:server")
