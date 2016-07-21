# ask user whether he wants (avg, max, min, sum, or exit)

import sqlite3

program_options = {'avg': "SELECT avg(num) FROM numbers",
					'max' : "SELECT max(num) FROM numbers",
					'min' : "SELECT min(num) FROM numbers",
					'sum' : "SELECT sum(num) FROM numbers"
					}

user_selection = (input("Do you want AVG, MAX, MIN, SUM, or EXIT?")).lower()

if user_selection not in program_options:
	exit()
else:
	with sqlite3.connect("newnum.db") as connection:
		c = connection.cursor()

		c.execute(program_options[user_selection])

		output = c.fetchone()

		print(user_selection + " " + str(output[0]))

