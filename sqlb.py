import sqlite3

conn = sqlite3.connect("cars.db")

c = conn.cursor()

c.execute("""CREATE TABLE inventory
			(Make TEXT, Model TEXT, Quantity INT)
			""")
c.close()