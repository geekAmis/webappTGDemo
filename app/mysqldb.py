import mysql.connector

class MySQLS(object):
	def __init__(self, db_config):
		super(MySQLS, self).__init__()
		self.db_config = db_config
		self.Conn()

	def checkConn(self):
		if self.conn.is_connected():
			self.cur = self.conn.cursor()
			return (True, "Успешное подключение к MySQL")
		else:
			return (False, "Ошибка подключения к базе данных MySQL.")

	def Conn(self):
		self.conn = mysql.connector.connect(**self.db_config)

	def disConn(self):
		self.conn.close()

	def get_Adminstructure(self):
		query = "SELECT TG_TOKEN, Balance, PAY_API, WebURL, Owners_Tids FROM Adminstructure"
		self.cur.execute(query)
		data = []
		for row in self.cur.fetchall():
			data.append({
				"TG_TOKEN": row[0],
				"Balance": row[1],
				"PAY_API": row[2],
				"WebURL": row[3],
				"Owners_Tids": row[4]
			})
		return data

	def getRows(self,table_name):
		query = "SELECT * FROM "+table_name
		self.cur.execute(query)
		cols = self.cur.fetchall()
		for row in cols:
			print(row)
		return cols

	# Добавление записи
	def add_record(self, table_name, data):
		columns = ', '.join(data.keys())
		values = ', '.join(['%s'] * len(data))
		query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
		self.cur.execute(query, list(data.values()))
		self.conn.commit()

	# Удаление записи
	def delete_record(self, table_name, condition):
		query = f"DELETE FROM {table_name} WHERE {condition}"
		self.cur.execute(query)
		self.conn.commit()

	# Редактирование записи
	def edit_record(self, table_name, data, condition):
		set_columns = ', '.join([f"{key} = %s" for key in data.keys()])
		query = f"UPDATE {table_name} SET {set_columns} WHERE {condition}"
		self.cur.execute(query, list(data.values()) + [condition])
		self.conn.commit()

	def check_table_row_exists(self, table_name, per, value):
		cols = self.getRows(table_name)
		return any(row[per] == value for row in cols)
		

config_db = {
	"host": "",
	"user": "",
	"password": "",
	"database": ""
}

""" EXAMPLE
------------------ADD ROW-------------------
new_record = {
	"TG_TOKEN": "new_token",
	"Balance": 1000,
	"PAY_API": "new_api",
	"WebURL": "https://new.url",
	"Owners_Tids": [1, 2, 3]
}
my_sql.add_record("Adminstructure", new_record)

-----------------DEL ROW--------------------
condition = "TG_TOKEN = 'old_token'"
my_sql.delete_record("Adminstructure", condition)

-----------------EDT ROW--------------------
updated_data = {
	"Balance": 2000,
	"PAY_API": "updated_api",
	"WebURL": "https://updated.url"
}
condition = "TG_TOKEN = 'old_token'"
my_sql.edit_record("Adminstructure", updated_data, condition)

-----------------CHK ROW-------------------
condition = "TG_TOKEN = 'old_token'"
if my_sql.check_table_row_exists("Adminstructure", condition):
	print("Запись с указанным параметром существует.")
else:
	print("Записи с указанным параметром не найдено.")
"""