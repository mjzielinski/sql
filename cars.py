import sqlite3


with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("CREATE TABLE inventory(make TEXT, model TEXT, quantity INT)")

	car_inventory = [
					('Ford', 'Tuarus', 20),
					('Honda', 'Civic', 13),
					('Chevrolet', 'Traverse', 1),
					('Subaru', 'Impreza', 5)
					]

	c.executemany("INSERT INTO inventory VALUES(?,?,?)", car_inventory)

c.close()