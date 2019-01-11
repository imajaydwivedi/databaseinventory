from django.contrib import admin
from django.contrib.admin import AdminSite
from mssql.models import Application, Server, Instance

# Register your models here.

# admin.site.register(Application)
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['serverid','servername','applicationid_id','environmenttype','fqdn','ipaddress','domain','isstandaloneserver','issqlclusternode','isagnode','iswsfc','issqlcluster','isag','parentserverid_id','os','spversion','isvm','isphysical','manufacturer','model','ram','cpu','powerplan','osarchitecture','isdecom','decomdate','generaldescription','collectiondate','collectedby','updateddate','updatedby']

    list_filter = ('environmenttype', 'domain', 'isdecom')

    search_fields = ['servername', 'serverid']
    pass


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    # pass
    list_display = ['instanceid','serverid_id','sqlinstance','instancename','rootdirectory','version','commonversion','build','versionstring','edition','collation','productkey','defaultdatalocation','defaultloglocation','defaultbackuplocation','errorlogpath','serviceaccount','port','isstandaloneinstance','issqlcluster','isaglistener','isagnode','aglistener','hasotherhasetup','harole','hapartner','ispowershelllinked','isdecom','decomdate','collectiondate','collectedby','updateddate','updatedby','remark1','remark2']

    list_filter = ['isdecom','versionstring', 'edition', 'harole']

    search_fields = ['sqlinstance']