from django.db import models
from django.urls import reverse

# Put tables within Distinct Category
databaseinventory = ['Application', 'Server', 'Instance']
# servermaintenance = ['Backupschedule', 'Commandqueue', 'Logging', 'Backuphistory']
# Performance Dashboard = []
# Service Requests = []

# Create your models here.


class Application(models.Model):
    # Field name made lowercase.
    applicationid = models.AutoField(
        db_column='ApplicationID', primary_key=True)
    # Field name made lowercase.
    applicationname = models.CharField(
        db_column='ApplicationName', max_length=125)
    # Field name made lowercase.
    businessunit = models.CharField(db_column='BusinessUnit', max_length=125)
    # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=125)
    # Field name made lowercase.
    priority = models.SmallIntegerField(
        db_column='Priority', blank=True, null=True)
    # Field name made lowercase.
    owner_emailid = models.CharField(db_column='Owner_EmailId', max_length=125)
    # Field name made lowercase.
    delegatedowner_emailid = models.CharField(
        db_column='DelegatedOwner_EmailId', max_length=125, blank=True, null=True)
    ownershipdelegationenddate = models.DateTimeField(
        db_column='OwnershipDelegationEndDate', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    primarycontact_emailid = models.CharField(
        db_column='PrimaryContact_EmailId', max_length=125)
    # Field name made lowercase.
    secondarycontact_emailid = models.CharField(
        db_column='SecondaryContact_EmailId', max_length=125, blank=True, null=True)
    # Field name made lowercase.
    secondarycontact2_emailid = models.CharField(
        db_column='SecondaryContact2_EmailId', max_length=125, blank=True, null=True)
    # Field name made lowercase.
    collectiontime = models.DateTimeField(db_column='CollectionTime')

    class Meta:
        managed = False
        db_table = 'Application'
        unique_together = (('applicationname', 'businessunit', 'product'),
                           ('applicationname', 'businessunit', 'product'),)

    def __str__(self):
        return "{0} ({1})".format(self.applicationname, self.applicationid)


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

    
