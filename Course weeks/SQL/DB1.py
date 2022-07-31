import sqlite3

connection = sqlite3.connect("db_1.db")

cursor=connection.cursor()


'''
cursor.execute("CREATE TABLE orders (order_id int, order_desc TEXT)")
cursor.execute("INSERT INTO orders VALUES (79,'xtl')")
cursor.execute("INSERT INTO orders VALUES (83,'68l')")
cursor.execute("INSERT INTO orders VALUES (89,'79l')")
'''
rows = cursor.execute("SELECT order_id,order_desc FROM orders").fetchall()

print(rows)

connection.commit()
'''
cursor.execute("INSERT INTO users VALUES (9,'Alex',1,'colxdx3')")
cursor.execute("INSERT INTO users VALUES (10,'Melanie',6,'sw3ds')")
cursor.execute("INSERT INTO users VALUES (11,'mat',3,'sw13q5')")



connection.commit()
'''


'''
rows = cursor.execute("SELECT name,age FROM users").fetchall()

print(rows[1])

'''

connection.close()
