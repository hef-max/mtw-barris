import mysql.connector as mysql

class Model():
	def __init__(self):
		self.db = mysql.connect(
			host="127.0.0.1",
			user="root",
			password="",
			database="test"
			)
		self.cursor = self.db.cursor()

	def read(self):
		self.cursor.execute("SELECT * FROM `jadwal_2`;")
		self.show = self.cursor.fetchall()
		return self.show

	def send(self, name, email, number, message):
		self.cursor.execute("INSERT INTO email VALUES (%s, %s, %s, %s)", (name, email, number, message, ))
		return self.db.commit()
