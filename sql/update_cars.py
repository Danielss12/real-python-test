import sqlite3

with sqlite3.connect('cars') as conn:
	c = conn.cursor()

	c.execute("UPDATE inventory SET Quantity = 10 WHERE Model = 'Civic' ")
	c.execute("UPDATE inventory SET Quantity = 15 WHERE Model = 'Focus' ")

	c.execute("SELECT * from inventory")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]