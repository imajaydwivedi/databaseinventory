from mssql.models import Server
servers_dict = Server.objects.all().values()
server_keys = servers_dict[0].keys()

columns = ''
for key in server_keys:
    columns += "'{0}',".format(key)


print(columns)