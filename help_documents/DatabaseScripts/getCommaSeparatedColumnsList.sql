DECLARE @columnList varchar(max);
set @columnList = Null;

SELECT @columnList = COALESCE(@columnList + ', ' + QUOTENAME(c.COLUMN_NAME,''''), QUOTENAME(c.COLUMN_NAME,''''))
FROM INFORMATION_SCHEMA.COLUMNS AS C
WHERE C.TABLE_NAME = 'Server'

PRINT @columnList	