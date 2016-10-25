import sqlite3

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	sql = {'Average':"SELECT avg(num) FROM numbers",
	'Maximum':"SELECT max(num) FROM numbers",
	'Minimum':"SELECT min(num) FROM numbers",
	'Sum':"SELECT sum(num) FROM numbers"}

	choice = raw_input("Choose aggregation to perform from(Average,Maximum,Minimum or Sum)...")

	for key, value in sql.iteritems():
		if key == choice:
			c.execute(value)
			result = c.fetchone()
			print result


