import sqlite3

conn = sqlite3.connect("csv.db")

c = conn.cursor()

try:
	c.execute("INSERT INTO employee VALUES('Brett',44)")
	c.execute("INSERT INTO employees VALUES('Taylor',646)")

	conn.commit()

except sqlite3.OperationalError:
	print "Ooooops!! Something went wrong!"

conn.close()