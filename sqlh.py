# add more data to existing table
# create new table and populate with data

import sqlite3

with sqlite3.connect("new.db") as connection:
	c= connection.cursor()

	cities = [
			('Boston', 'MA', 600000),
			('Los Angeles', 'CA', 38000000),
			('Houston', 'TX', 2100000),
			('Philadelphia', 'PA', 1500000),
			('San Antonio', 'TX', 1400000),
			('San Diego', 'CA', 130000),
			('Dallas', 'TX', 1200000),
			('San Jose', 'CA', 900000),
			('Jacksonville', 'FL', 800000),
			('Indianapolis', 'IN', 800000),
			('Austin', 'TX', 800000),
			('Detroit', 'MI', 700000)
			]

	c.executemany("INSERT INTO population VALUES(?,?,?)", cities)

	c.execute("SELECT * FROM population where population > 10000000")

	rows = c.fetchall()

	for r in rows:
		print (r[0], r[1], r[2])

	print("\n")

	c.execute("CREATE TABLE regions(city TEXT, region TEXT)")

	region_data = [
				('New York City', 'Northeast'),
				('San Francisco', 'West'),
				('Chicago', 'Midwest'),
				('Houston', 'South'),
				('Phoenix', 'West'),
				('Boston', 'Northeast'),
				('Los Angeles', 'West'),
				('Houston', 'South'),
				('Philadelphia', 'Northeast'),
				('San Antonio', 'South'),
				('San Diego', 'West'),
				('Dallas', 'South'),
				('San Jose', 'West'),
				('Jacksonville', 'South'),
				('Indianapolis', 'Midwest'),
				('Austin', 'South'),
				('Detroit', 'Midwest')
				]

	c.executemany("INSERT INTO regions VALUES(?,?)", region_data)

	c.execute("SELECT * FROM regions ORDER BY region ASC")

	rows = c.fetchall()

	for r in rows:
		print(r[0],r[1])

	c.close()
