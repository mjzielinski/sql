# add some new cars to inventory

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	new_inventory = [
					('Ford', 'Car A', 5),
					('Ford', 'Car B', 4),
					('Ford', 'Car C', 3),
					('Honda', 'Car D', 2),
					('Honda', 'Car E', 1)
					]

	c.executemany("INSERT INTO inventory VALUES(?,?,?)", new_inventory)
	c.close()