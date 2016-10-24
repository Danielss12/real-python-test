import sqlite3

with sqlite3.connect("cars") as conn:
	c = conn.cursor()

	c.execute("SELECT  Make, Model, Quantity from inventory WHERE Make = 'Ford'")

	rows = c.fetchall()

	for r in rows:
		print r[0],r[1],r[2]