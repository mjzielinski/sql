import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("""SELECT DISTINCT inventory.make, inventory.model, count(orders.order_date)
				FROM inventory, orders WHERE inventory.model = orders.model""")

	data = c.fetchall()

	for row in data:
		print (row[0], row[1], row[2])