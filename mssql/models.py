from django.db import models
from django.urls import reverse
from django.utils import timezone

# Put tables within Distinct Category
databaseinventory = ['Application', 'Server', 'Instance', 'Database']
servermaintenance = ['Backupschedule', 'Commandqueue', 'Logging', 'Backuphistory']
# Performance Dashboard = []
# Service Requests = []

# Create your models here.

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
    collectiondate = models.DateTimeField(db_column='CollectionDate', blank=True, null=True, default=timezone.now())  # Field name made lowercase.
    collectedby = models.CharField(db_column='CollectedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Application'
        unique_together = (('category', 'businessunit', 'applicationname', 'businessowner', 'technicalowner', 'secondarytechnicalowner'),)

    def __str__(self):
        displayName = None
        if (self.applicationname):
            displayName = self.applicationname
        elif (self.businessunit):
            displayName = self.businessunit
        else:
            displayName = self.category

        return "{0}  ({1})".format(displayName, self.applicationid)

    def get_absolute_url(self):
        return reverse("mssql:applicationdetail", kwargs={"pk": self.pk})



class Server(models.Model):
    # Field name made lowercase.
    serverid = models.AutoField(db_column='ServerID', primary_key=True)
    # Field name made lowercase.
    servername = models.CharField(
        db_column='ServerName', unique=True, max_length=50)
    # Field name made lowercase.
    applicationid = models.ForeignKey(
        Application, models.DO_NOTHING, db_column='ApplicationId', blank=True, null=True, related_name='servers')
    ENVTYPE_CHOICES = (
        ('NA', 'Not Available'),
        ('Dev', 'Dev'),
        ('QA', 'QA'),
        ('Test', 'Test'),
        ('UAT', 'UAT'),
        ('Prod', 'Prod'),
    )
    # Field name made lowercase.
    environmenttype = models.CharField(
        db_column='EnvironmentType', max_length=4, blank=True, null=True, choices=ENVTYPE_CHOICES)
    # Field name made lowercase.
    fqdn = models.CharField(db_column='FQDN', unique=True, max_length=125)
    # Field name made lowercase.
    ipaddress = models.CharField(
        db_column='IPAddress', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    DOMAIN_CHOICES = (
        ('corporate.local', 'Corporate'),
        ('armus', 'Armus'),
        ('angoss', 'Angoss'),
        ('dmz', 'DMZ'),
        ('NA', 'Not Available'),
    )
    domain = models.CharField(
        db_column='Domain', max_length=30, blank=True, null=True, choices=DOMAIN_CHOICES)
    # Field name made lowercase.
    isstandaloneserver = models.BooleanField(
        db_column='IsStandaloneServer', blank=True, null=True)
    # Field name made lowercase.
    issqlclusternode = models.BooleanField(
        db_column='IsSqlClusterNode', blank=True, null=True)
    # Field name made lowercase.
    isagnode = models.BooleanField(db_column='IsAgNode', blank=True, null=True)
    # Field name made lowercase.
    iswsfc = models.BooleanField(db_column='IsWSFC', blank=True, null=True)
    # Field name made lowercase.
    issqlcluster = models.BooleanField(
        db_column='IsSqlCluster', blank=True, null=True)
    # Field name made lowercase.
    isag = models.BooleanField(db_column='IsAG', blank=True, null=True)
    # Field name made lowercase.
    parentserverid = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='ParentServerId', blank=True, null=True, related_name='sqlnetworknames')
    # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=125,
                          blank=True, null=True)
    # Field name made lowercase.
    spversion = models.CharField(
        db_column='SPVersion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    isvm = models.BooleanField(db_column='IsVM', blank=True, null=True)
    # Field name made lowercase.
    isphysical = models.BooleanField(
        db_column='IsPhysical', blank=True, null=True)
    # Field name made lowercase.
    manufacturer = models.CharField(
        db_column='Manufacturer', max_length=125, blank=True, null=True)
    # Field name made lowercase.
    model = models.CharField(
        db_column='Model', max_length=125, blank=True, null=True)
    # Field name made lowercase.
    ram = models.IntegerField(db_column='RAM', blank=True, null=True)
    # Field name made lowercase.
    cpu = models.SmallIntegerField(db_column='CPU', blank=True, null=True)
    # Field name made lowercase.
    powerplan = models.CharField(
        db_column='Powerplan', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    osarchitecture = models.CharField(
        db_column='OSArchitecture', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    isdecom = models.BooleanField(db_column='ISDecom', blank=True, null=True)
    # Field name made lowercase.
    decomdate = models.DateTimeField(
        db_column='DecomDate', blank=True, null=True)
    # Field name made lowercase.
    generaldescription = models.TextField(
        db_column='GeneralDescription', blank=True, null=True)
    remark1 = models.TextField(
        db_column='Remark1', blank=True, null=True
    )
    remark2 = models.TextField(
        db_column='Remark2', blank=True, null=True
    )
    # Field name made lowercase.
    collectiondate = models.DateTimeField(
        db_column='CollectionDate', blank=True, null=True)
    # Field name made lowercase.
    collectedby = models.CharField(
        db_column='CollectedBy', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    updateddate = models.DateTimeField(
        db_column='UpdatedDate', blank=True, null=True)
    # Field name made lowercase.
    updatedby = models.CharField(
        db_column='UpdatedBy', max_length=50, blank=True, null=True)

    def __str__(self):
        return "{0}  ({1})".format(self.servername, self.serverid)

    def get_absolute_url(self):
        return reverse("mssql:serverdetail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'Server'


class Instance(models.Model):
    # Field name made lowercase.
    instanceid = models.AutoField(db_column='InstanceID', primary_key=True)
    # Field name made lowercase.
    serverid = models.ForeignKey(
        'Server', models.DO_NOTHING, db_column='ServerID', related_name='sqlinstances')
    # Field name made lowercase.
    sqlinstance = models.CharField(
        db_column='SqlInstance', unique=True, max_length=125)
    # Field name made lowercase.
    instancename = models.CharField(db_column='InstanceName', max_length=50)
    # Field name made lowercase.
    rootdirectory = models.CharField(
        db_column='RootDirectory', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=15)
    # Field name made lowercase.
    commonversion = models.CharField(
        db_column='CommonVersion', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    build = models.IntegerField(db_column='Build', blank=True, null=True)
    # Field name made lowercase.
    versionstring = models.CharField(
        db_column='VersionString', max_length=125, blank=True, null=True)
    # Field name made lowercase.
    edition = models.CharField(db_column='Edition', max_length=50)
    # Field name made lowercase.
    collation = models.CharField(
        db_column='Collation', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    productkey = models.CharField(
        db_column='ProductKey', max_length=29, blank=True, null=True)
    # Field name made lowercase.
    defaultdatalocation = models.CharField(
        db_column='DefaultDataLocation', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    defaultloglocation = models.CharField(
        db_column='DefaultLogLocation', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    defaultbackuplocation = models.CharField(
        db_column='DefaultBackupLocation', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    errorlogpath = models.CharField(
        db_column='ErrorLogPath', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    serviceaccount = models.CharField(
        db_column='ServiceAccount', max_length=125, blank=True, null=True)
    # Field name made lowercase.
    port = models.CharField(
        db_column='Port', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    isstandaloneinstance = models.BooleanField(
        db_column='IsStandaloneInstance')
    # Field name made lowercase.
    issqlcluster = models.BooleanField(db_column='IsSQLCluster')
    # Field name made lowercase.
    isaglistener = models.BooleanField(db_column='IsAGListener')
    # Field name made lowercase.
    isagnode = models.BooleanField(db_column='IsAGNode')
    aglistener = models.ForeignKey('self', models.DO_NOTHING, db_column='AGListener',
                                   blank=True, null=True, related_name='aglisteners')  # Field name made lowercase.
    # Field name made lowercase.
    hasotherhasetup = models.BooleanField(db_column='HasOtherHASetup')
    # Field name made lowercase.
    harole = models.CharField(
        db_column='HARole', max_length=20, blank=True, null=True)
    hapartner = models.ForeignKey('self', models.DO_NOTHING, db_column='HAPartner',
                                  blank=True, null=True, related_name='hapartners')  # Field name made lowercase.
    # Field name made lowercase.
    ispowershelllinked = models.BooleanField(
        db_column='IsPowershellLinked', blank=True, null=True)
    # Field name made lowercase.
    isdecom = models.BooleanField(
        db_column='IsDecom', default=False, blank=True, null=True)
    # Field name made lowercase.
    decomdate = models.DateTimeField(
        db_column='DecomDate', blank=True, null=True)
    # Field name made lowercase.
    collectiondate = models.DateTimeField(
        db_column='CollectionDate', blank=True, null=True)
    # Field name made lowercase.
    collectedby = models.CharField(db_column='CollectedBy', max_length=50)
    # Field name made lowercase.
    updateddate = models.DateTimeField(
        db_column='UpdatedDate', blank=True, null=True)
    # Field name made lowercase.
    updatedby = models.CharField(
        db_column='UpdatedBy', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    remark1 = models.TextField(db_column='Remark1', blank=True, null=True)
    # Field name made lowercase.
    remark2 = models.TextField(db_column='Remark2', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Instance'

    def __str__(self):
        return "{0}  ({1})".format(self.instanceid, self.sqlinstance)

    def get_absolute_url(self):
        return reverse("mssql:instancedetail", kwargs={"pk": self.pk})



class Database(models.Model):
    # Field name made lowercase.
    databaseid = models.AutoField(db_column='DatabaseId', primary_key=True)
    # Field name made lowercase.
    instanceid = models.ForeignKey(
        'Instance', models.DO_NOTHING, db_column='InstanceId')
    # Field name made lowercase.
    databasename = models.CharField(db_column='DatabaseName', max_length=50)
    # Field name made lowercase.
    createddate = models.DateTimeField(
        db_column='CreatedDate', blank=True, null=True)
    # Field name made lowercase.
    RECOVERYMODEL_CHOICES = (
        ('Simple', 'Simple'),
        ('Bulk-Logged', 'Bulk-Logged'),
        ('Full', 'Full'),
    )
    recoverymodel = models.CharField(
        db_column='RecoveryModel', max_length=64, blank=True, null=True, choices=RECOVERYMODEL_CHOICES, default='Full')
    # Field name made lowercase.
    currentdbsize = models.CharField(
        db_column='CurrentDBSize', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    backuppath = models.CharField(
        db_column='BackupPath', max_length=128, blank=True, null=True)
    
    # Custom fields start here
    # sqlinstance = models.ForeignKey(
    #     'Instance', models.DO_NOTHING, db_column='InstanceName')

    class Meta:
        managed = False
        db_table = 'Databases'

    def __str__(self):
        # return self.databasename
        return "{}  ({})".format(self.databasename, self.databaseid)

    def get_absolute_url(self):
        return reverse("mssql:databasedetail", kwargs={"pk": self.pk})


class Backupschedule(models.Model):
    # Field name made lowercase.
    bkuschedid = models.AutoField(db_column='BkuSchedId', primary_key=True)
    # Field name made lowercase.
    instanceid = models.ForeignKey(
        'Instance', models.DO_NOTHING, db_column='InstanceId')
    # Field name made lowercase.
    timefrom = models.TimeField(db_column='TimeFrom', blank=True, null=True)
    # Field name made lowercase.
    timeto = models.TimeField(db_column='TimeTo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BackupSchedule'

    def __str__(self):
        return self.bkuschedid + '  (' + str(self.timefrom) + ' - ' + str(self.timeto) + ')'

    def get_absolute_url(self):
        return reverse("mssql:backupscheduledetail", kwargs={"pk": self.pk})


class Commandqueue(models.Model):
    # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=254)
    # Field name made lowercase.
    instanceid = models.ForeignKey(
        'Instance', models.DO_NOTHING, db_column='InstanceId',related_name='sqlinstances')
    # Field name made lowercase.
    databaseid = models.ForeignKey(
        'Database', models.DO_NOTHING, db_column='DatabaseId', related_name='databases')
    # Field name made lowercase.
    command = models.TextField(db_column='Command')
    # Field name made lowercase.
    jobid = models.CharField(
        db_column='jobId', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    JOBTYPE_CHOICES = (
        ('BKU','BKU'),
        ('NA','Not Available'),
    )
    jobtype = models.CharField(db_column='JobType', max_length=20,choices = JOBTYPE_CHOICES, default='BKU')
    # Field name made lowercase.
    STATUS_CHOICES = (
        ('Scheduled','Scheduled'),
        ('NA','Not Available'),
    )
    status = models.CharField(db_column='Status', max_length=10, choices=STATUS_CHOICES, default = 'Scheduled')
    reason = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'CommandQueue'

    def get_absolute_url(self):
        return reverse("mssql:commandqueuedetail", kwargs={"pk": self.pk})


class Logging(models.Model):
    # Field name made lowercase.
    logid = models.AutoField(db_column='logId', primary_key=True)
    # Field name made lowercase.
    logmessage = models.TextField(db_column='LogMessage')

    class Meta:
        managed = False
        db_table = 'Logging'

    def get_absolute_url(self):
        return reverse("mssql:loggingdetail", kwargs={"pk": self.pk})


class Backuphistory(models.Model):
    # Field name made lowercase.
    backuphistid = models.AutoField(db_column='BackupHistId', primary_key=True)
    # Field name made lowercase.
    instanceid = models.ForeignKey(
        'Instance', models.DO_NOTHING, db_column='InstanceId')
    # Field name made lowercase.
    databaseid = models.ForeignKey(
        'Database', models.DO_NOTHING, db_column='DatabaseId')
    # Field name made lowercase.
    fullbackupdate = models.DateTimeField(
        db_column='FullbackupDate', blank=True, null=True)
    # Field name made lowercase.
    diffbackupdate = models.DateTimeField(
        db_column='DiffBackupDate', blank=True, null=True)
    # Field name made lowercase.
    tranbackupdate = models.DateTimeField(
        db_column='TranBackupDate', blank=True, null=True)
    # Field name made lowercase.
    fullbackupsize = models.DecimalField(
        db_column='FullBackupSize', max_digits=20, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    diffbackupsize = models.DecimalField(
        db_column='DiffBackupSize', max_digits=20, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    tranbackupsize = models.DecimalField(
        db_column='TranBackupSize', max_digits=20, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    fullbackupduration = models.IntegerField(
        db_column='FullBackupDuration', blank=True, null=True)
    # Field name made lowercase.
    diffbackupduration = models.IntegerField(
        db_column='DiffBackupDuration', blank=True, null=True)
    # Field name made lowercase.
    tranbackupduration = models.IntegerField(
        db_column='TranBackupDuration', blank=True, null=True)
    # Field name made lowercase.
    compressed = models.BooleanField(
        db_column='Compressed', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BackupHistory'

    def get_absolute_url(self):
        return reverse("mssql:backuphistorydetail", kwargs={"pk": self.pk})