# update quantity on two of the records
# output all records from table
# output just the Ford vehicles

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("UPDATE inventory SET quantity=100 WHERE model='Car E'")
	c.execute("UPDATE inventory SET quantity=101 WHERE model='Car D'")

	
	c.execute("SELECT * from inventory WHERE make='Ford'")
	rows = c.fetchall()

	print("\nFORD INVENTORY\n")
	for r in rows:
		print(r[0], r[1], r[2])

	c.execute("SELECT * from inventory")
	rows = c.fetchall()

	print("\nALL INVENTORY\n")
	for r in rows:
		print(r[0],r[1],r[2])

	c.close()