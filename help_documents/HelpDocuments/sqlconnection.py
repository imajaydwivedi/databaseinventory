import pyodbc 
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=tul1dbapmtdb1;'
                      'Database=SQLDBATools;'
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()
cursor.execute('SELECT @@servername,db_name()')

for row in cursor:
    print(row)