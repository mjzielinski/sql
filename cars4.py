import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date TEXT)")

	new_orders = [
				('Honda', 'Car E', '01/01/2016'),
				('Honda', 'Car E', '01/01/2016'),
				('Honda', 'Car D', '01/01/2016'),
				('Honda', 'Car D', '01/01/2016'),
				('Honda', 'Car E', '01/01/2016'),
				('Honda', 'Car E', '01/01/2016'),
				('Ford', 'Car B', '01/01/2016'),
				('Honda', 'Car E', '01/01/2016'),
				('Ford', 'Car A', '01/01/2016'),
				('Ford', 'Car C', '01/01/2016'),
				('Honda', 'Car E', '01/01/2016'),
				('Honda', 'Car E', '01/01/2016'),
				('Honda', 'Car E', '01/01/2016'),
				('Honda', 'Car E', '01/01/2016')
				]

	c.executemany("INSERT INTO orders VALUES(?,?,?)", new_orders)

	c.execute("""SELECT inventory.make, inventory.model, inventory.quantity, orders.order_date
				FROM inventory INNER JOIN orders on inventory.model = orders.model""")
	data = c.fetchall()

	for row in data:
		print (row[0], row[1])
		print (row[2])
		print (row[3])
		print


	c.close()

