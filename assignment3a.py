# add 100 random integers, ranging from 0 to 100, into a new database

import sqlite3
from random import randint

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	c.execute("DROP TABLE if exists numbers")
	c.execute("CREATE TABLE numbers(num INT)")

	for num in range(100):
		c.execute("INSERT INTO numbers VALUES(?)", (randint(0,100),))

	c.close()