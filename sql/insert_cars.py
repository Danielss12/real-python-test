import sqlite3

with sqlite3.connect("cars") as conn:
	c = conn.cursor()

	cars_list = [('Ford','Focus',10),('Ford','Mustang',15),('Ford','Aquele',2),('Honda','Civic',22),
	('Honda','Algum',2)]

	c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars_list)

	