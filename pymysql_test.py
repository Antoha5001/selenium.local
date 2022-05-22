import pymysql


host = 'localhost'
user = 'pythonless'
password = 'pythonless'
db_name = '623030'

connector = pymysql.connect(host=host, user=user, password=password, database=db_name)

with connector.cursor() as cursor:
	select_all = "delete from listovki"
	
	cursor.execute(select_all)
	connector.commit()

with connector.cursor() as cursor:
	select_all = "select * from listovki"
	
	cursor.execute(select_all)

	rows = cursor.fetchall()

	print(rows)