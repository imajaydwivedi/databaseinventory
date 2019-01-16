from mssql.models import Application , Server, Instance, Database, Backupschedule, Commandqueue, Logging
servers_dict = Logging.objects.all().values()
server_keys = servers_dict[0].keys()

columns = ''
for key in server_keys:
    columns += "'{0}',".format(key)


print(columns)