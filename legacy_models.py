# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Application(models.Model):
    applicationid = models.AutoField(db_column='ApplicationID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=125)  # Field name made lowercase.
    businessunit = models.CharField(db_column='BusinessUnit', max_length=125)  # Field name made lowercase.
    applicationname = models.CharField(db_column='ApplicationName', max_length=125, blank=True, null=True)  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    businessowner = models.CharField(db_column='BusinessOwner', max_length=125, blank=True, null=True)  # Field name made lowercase.
    technicalowner = models.CharField(db_column='TechnicalOwner', max_length=125, blank=True, null=True)  # Field name made lowercase.
    secondarytechnicalowner = models.CharField(db_column='SecondaryTechnicalOwner', max_length=125, blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectiondate = models.DateTimeField(db_column='CollectionDate', blank=True, null=True)  # Field name made lowercase.
    collectedby = models.CharField(db_column='CollectedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Application'
        unique_together = (('category', 'businessunit', 'applicationname', 'businessowner', 'technicalowner', 'secondarytechnicalowner'),)


class Backuphistory(models.Model):
    backuphistid = models.AutoField(db_column='BackupHistId', primary_key=True)  # Field name made lowercase.
    instanceid = models.ForeignKey('InstanceOld', models.DO_NOTHING, db_column='InstanceId')  # Field name made lowercase.
    databaseid = models.ForeignKey('Databases', models.DO_NOTHING, db_column='DatabaseId')  # Field name made lowercase.
    fullbackupdate = models.DateTimeField(db_column='FullbackupDate', blank=True, null=True)  # Field name made lowercase.
    diffbackupdate = models.DateTimeField(db_column='DiffBackupDate', blank=True, null=True)  # Field name made lowercase.
    tranbackupdate = models.DateTimeField(db_column='TranBackupDate', blank=True, null=True)  # Field name made lowercase.
    fullbackupsize = models.DecimalField(db_column='FullBackupSize', max_digits=20, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    diffbackupsize = models.DecimalField(db_column='DiffBackupSize', max_digits=20, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tranbackupsize = models.DecimalField(db_column='TranBackupSize', max_digits=20, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fullbackupduration = models.IntegerField(db_column='FullBackupDuration', blank=True, null=True)  # Field name made lowercase.
    diffbackupduration = models.IntegerField(db_column='DiffBackupDuration', blank=True, null=True)  # Field name made lowercase.
    tranbackupduration = models.IntegerField(db_column='TranBackupDuration', blank=True, null=True)  # Field name made lowercase.
    compressed = models.BooleanField(db_column='Compressed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BackupHistory'


class Backupschedule(models.Model):
    bkuschedid = models.AutoField(db_column='BkuSchedId', primary_key=True)  # Field name made lowercase.
    instanceid = models.ForeignKey('InstanceOld', models.DO_NOTHING, db_column='InstanceId')  # Field name made lowercase.
    timefrom = models.TimeField(db_column='TimeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.TimeField(db_column='TimeTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BackupSchedule'


class Commandqueue(models.Model):
    guid = models.CharField(db_column='GUID', max_length=254)  # Field name made lowercase.
    instanceid = models.ForeignKey('InstanceOld', models.DO_NOTHING, db_column='InstanceId')  # Field name made lowercase.
    databaseid = models.ForeignKey('Databases', models.DO_NOTHING, db_column='DatabaseId')  # Field name made lowercase.
    command = models.TextField(db_column='Command')  # Field name made lowercase.
    jobid = models.CharField(db_column='jobId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jobtype = models.CharField(db_column='JobType', max_length=20)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    reason = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CommandQueue'


class Databases(models.Model):
    databaseid = models.AutoField(db_column='DatabaseId', primary_key=True)  # Field name made lowercase.
    instanceid = models.ForeignKey('Instance', models.DO_NOTHING, db_column='InstanceId')  # Field name made lowercase.
    databasename = models.CharField(db_column='DatabaseName', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    recoverymodel = models.CharField(db_column='RecoveryModel', max_length=64, blank=True, null=True)  # Field name made lowercase.
    currentdbsize = models.CharField(db_column='CurrentDBSize', max_length=10, blank=True, null=True)  # Field name made lowercase.
    backuppath = models.CharField(db_column='BackupPath', max_length=128, blank=True, null=True)  # Field name made lowercase.
    instanceid_old = models.IntegerField(db_column='InstanceId_old', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Databases'


class Instance(models.Model):
    instanceid = models.AutoField(db_column='InstanceID', primary_key=True)  # Field name made lowercase.
    serverid = models.ForeignKey('Server', models.DO_NOTHING, db_column='ServerID')  # Field name made lowercase.
    sqlinstance = models.CharField(db_column='SqlInstance', unique=True, max_length=125)  # Field name made lowercase.
    instancename = models.CharField(db_column='InstanceName', max_length=50)  # Field name made lowercase.
    rootdirectory = models.CharField(db_column='RootDirectory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=15, blank=True, null=True)  # Field name made lowercase.
    commonversion = models.CharField(db_column='CommonVersion', max_length=5, blank=True, null=True)  # Field name made lowercase.
    build = models.IntegerField(db_column='Build', blank=True, null=True)  # Field name made lowercase.
    versionstring = models.CharField(db_column='VersionString', max_length=125, blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='Edition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collation = models.CharField(db_column='Collation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    productkey = models.CharField(db_column='ProductKey', max_length=29, blank=True, null=True)  # Field name made lowercase.
    defaultdatalocation = models.CharField(db_column='DefaultDataLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    defaultloglocation = models.CharField(db_column='DefaultLogLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    defaultbackuplocation = models.CharField(db_column='DefaultBackupLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    errorlogpath = models.CharField(db_column='ErrorLogPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    serviceaccount = models.CharField(db_column='ServiceAccount', max_length=125, blank=True, null=True)  # Field name made lowercase.
    port = models.CharField(db_column='Port', max_length=6, blank=True, null=True)  # Field name made lowercase.
    isstandaloneinstance = models.BooleanField(db_column='IsStandaloneInstance', blank=True, null=True)  # Field name made lowercase.
    issqlcluster = models.BooleanField(db_column='IsSQLCluster', blank=True, null=True)  # Field name made lowercase.
    isaglistener = models.BooleanField(db_column='IsAGListener', blank=True, null=True)  # Field name made lowercase.
    isagnode = models.BooleanField(db_column='IsAGNode', blank=True, null=True)  # Field name made lowercase.
    aglistener = models.ForeignKey('self', models.DO_NOTHING, db_column='AGListener', blank=True, null=True)  # Field name made lowercase.
    hasotherhasetup = models.BooleanField(db_column='HasOtherHASetup', blank=True, null=True)  # Field name made lowercase.
    harole = models.CharField(db_column='HARole', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hapartner = models.ForeignKey('self', models.DO_NOTHING, db_column='HAPartner', blank=True, null=True)  # Field name made lowercase.
    ispowershelllinked = models.BooleanField(db_column='IsPowershellLinked', blank=True, null=True)  # Field name made lowercase.
    isdecom = models.BooleanField(db_column='IsDecom', blank=True, null=True)  # Field name made lowercase.
    decomdate = models.DateTimeField(db_column='DecomDate', blank=True, null=True)  # Field name made lowercase.
    collectiondate = models.DateTimeField(db_column='CollectionDate', blank=True, null=True)  # Field name made lowercase.
    collectedby = models.CharField(db_column='CollectedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark1 = models.TextField(db_column='Remark1', blank=True, null=True)  # Field name made lowercase.
    remark2 = models.TextField(db_column='Remark2', blank=True, null=True)  # Field name made lowercase.
    maxjobcount = models.IntegerField(db_column='maxJobCount', blank=True, null=True)  # Field name made lowercase.
    defaultbkupathsize = models.CharField(db_column='DefaultBkuPathSize', max_length=20, blank=True, null=True)  # Field name made lowercase.
    defaultbkupathfree = models.CharField(db_column='DefaultBkuPathFree', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Instance'


class InstanceOld(models.Model):
    instanceid = models.AutoField(db_column='InstanceID', primary_key=True)  # Field name made lowercase.
    instancename = models.CharField(db_column='InstanceName', max_length=128)  # Field name made lowercase.
    serverid = models.ForeignKey('ServerOld', models.DO_NOTHING, db_column='ServerID')  # Field name made lowercase.
    port = models.CharField(db_column='Port', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sqlserviceaccountid = models.IntegerField(db_column='SQLServiceAccountID', blank=True, null=True)  # Field name made lowercase.
    authenticationmode = models.BooleanField(db_column='AuthenticationMode', blank=True, null=True)  # Field name made lowercase.
    saaccountname = models.CharField(db_column='saAccountName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    saaccountpassword = models.CharField(db_column='saAccountPassword', max_length=64, blank=True, null=True)  # Field name made lowercase.
    instanceclassification = models.SmallIntegerField(db_column='InstanceClassification', blank=True, null=True)  # Field name made lowercase.
    instancecores = models.SmallIntegerField(db_column='InstanceCores', blank=True, null=True)  # Field name made lowercase.
    instanceram = models.BigIntegerField(db_column='InstanceRAM', blank=True, null=True)  # Field name made lowercase.
    sqlserveragentaccountid = models.IntegerField(db_column='SQLServerAgentAccountID', blank=True, null=True)  # Field name made lowercase.
    defaultbkupath = models.CharField(db_column='DefaultBkuPath', max_length=250, blank=True, null=True)  # Field name made lowercase.
    defaultbkupathsize = models.CharField(db_column='DefaultBkuPathSize', max_length=20, blank=True, null=True)  # Field name made lowercase.
    defaultbkupathfree = models.CharField(db_column='DefaultBkuPathFree', max_length=20, blank=True, null=True)  # Field name made lowercase.
    maxjobcount = models.IntegerField(db_column='maxJobCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Instance_old'


class Logging(models.Model):
    logid = models.AutoField(db_column='logId', primary_key=True)  # Field name made lowercase.
    logmessage = models.TextField(db_column='LogMessage')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Logging'


class Sqlsyntax(models.Model):
    syntaxid = models.AutoField(db_column='SyntaxID')  # Field name made lowercase.
    sqlversion = models.CharField(db_column='SQLVersion', max_length=128)  # Field name made lowercase.
    sqltype = models.CharField(db_column='SQLType', max_length=10)  # Field name made lowercase.
    sqlsyntax = models.TextField(db_column='SQLSyntax')  # Field name made lowercase.
    syntaxtype = models.CharField(db_column='SyntaxType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sqlparams = models.CharField(db_column='SQLParams', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SQLSyntax'


class Server(models.Model):
    serverid = models.AutoField(db_column='ServerID', primary_key=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', unique=True, max_length=50)  # Field name made lowercase.
    applicationid = models.ForeignKey(Application, models.DO_NOTHING, db_column='ApplicationId', blank=True, null=True)  # Field name made lowercase.
    environmenttype = models.CharField(db_column='EnvironmentType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fqdn = models.CharField(db_column='FQDN', unique=True, max_length=125)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=15, blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=30, blank=True, null=True)  # Field name made lowercase.
    isstandaloneserver = models.BooleanField(db_column='IsStandaloneServer', blank=True, null=True)  # Field name made lowercase.
    issqlclusternode = models.BooleanField(db_column='IsSqlClusterNode', blank=True, null=True)  # Field name made lowercase.
    isagnode = models.BooleanField(db_column='IsAgNode', blank=True, null=True)  # Field name made lowercase.
    iswsfc = models.BooleanField(db_column='IsWSFC', blank=True, null=True)  # Field name made lowercase.
    issqlcluster = models.BooleanField(db_column='IsSqlCluster', blank=True, null=True)  # Field name made lowercase.
    isag = models.BooleanField(db_column='IsAG', blank=True, null=True)  # Field name made lowercase.
    parentserverid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentServerId', blank=True, null=True)  # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=125, blank=True, null=True)  # Field name made lowercase.
    spversion = models.CharField(db_column='SPVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isvm = models.BooleanField(db_column='IsVM', blank=True, null=True)  # Field name made lowercase.
    isphysical = models.BooleanField(db_column='IsPhysical', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=125, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=125, blank=True, null=True)  # Field name made lowercase.
    ram = models.IntegerField(db_column='RAM', blank=True, null=True)  # Field name made lowercase.
    cpu = models.SmallIntegerField(db_column='CPU', blank=True, null=True)  # Field name made lowercase.
    powerplan = models.CharField(db_column='Powerplan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osarchitecture = models.CharField(db_column='OSArchitecture', max_length=6, blank=True, null=True)  # Field name made lowercase.
    isdecom = models.BooleanField(db_column='ISDecom', blank=True, null=True)  # Field name made lowercase.
    decomdate = models.DateTimeField(db_column='DecomDate', blank=True, null=True)  # Field name made lowercase.
    generaldescription = models.TextField(db_column='GeneralDescription', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectiondate = models.DateTimeField(db_column='CollectionDate', blank=True, null=True)  # Field name made lowercase.
    collectedby = models.CharField(db_column='CollectedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    backuppsdeployed = models.BooleanField(db_column='BackupPSDeployed', blank=True, null=True)  # Field name made lowercase.
    sqltype = models.CharField(db_column='SQLType', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Server'


class ServerOld(models.Model):
    serverid = models.IntegerField(db_column='ServerID', primary_key=True)  # Field name made lowercase.
    server = models.CharField(db_column='Server', max_length=128, blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=25, blank=True, null=True)  # Field name made lowercase.
    servertype = models.CharField(db_column='ServerType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='ShortDescription', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sqlstate = models.CharField(db_column='SQLState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)  # Field name made lowercase.
    businessunit = models.CharField(db_column='BusinessUnit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    sqlversion = models.CharField(db_column='SQLVersion', max_length=64, blank=True, null=True)  # Field name made lowercase.
    sockets = models.IntegerField(db_column='Sockets', blank=True, null=True)  # Field name made lowercase.
    cores = models.IntegerField(db_column='Cores', blank=True, null=True)  # Field name made lowercase.
    logicalprocs = models.IntegerField(db_column='LogicalProcs', blank=True, null=True)  # Field name made lowercase.
    businessowner = models.CharField(db_column='Businessowner', max_length=25, blank=True, null=True)  # Field name made lowercase.
    technicalowner = models.CharField(db_column='TechnicalOwner', max_length=25, blank=True, null=True)  # Field name made lowercase.
    secondarytechnicalowner = models.CharField(db_column='SecondaryTechnicalOwner', max_length=25, blank=True, null=True)  # Field name made lowercase.
    additionalnotes = models.TextField(db_column='AdditionalNotes', blank=True, null=True)  # Field name made lowercase.
    backuppsdeployed = models.BooleanField(db_column='BackupPSDeployed', blank=True, null=True)  # Field name made lowercase.
    sqltype = models.CharField(db_column='SQLType', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Server_old'
