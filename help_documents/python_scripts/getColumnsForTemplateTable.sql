declare @objectName varchar(50) = 'server'
select	[list_tableHeaders] = '<th scope="col">'+c.name+'</th>',
		[list_tableData] = '<td>{{'+@objectName+'.'+LOWER(REPLACE(c.name,'_',''))+'}}</td>',
		[detail_tableData] = case	when c.column_id%2=1 then '<tr class="bg-transpart"><td>'+c.name+'</td><td>{{'+@objectName+'_detail.'+LOWER(REPLACE(c.name,'_',''))+'}}</td></tr>'
									else '<tr class="bg-light"><td>'+c.name+'</td><td>{{'+@objectName+'_detail.'+LOWER(REPLACE(c.name,'_',''))+'}}</td></tr>'
									end
from  sys.columns c WHERE OBJECT_NAME(c.object_id) = @objectName
order by c.column_id asc