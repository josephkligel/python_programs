import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
# c.execute("""CREATE TABLE IF NOT EXISTS persons (
#     first_name TEXT,
#     last_name TEXT,
#     age INTEGER
#     )""")
# c.execute("""INSERT INTO persons VALUES
#     ('John', 'Smith', 25),
#     ('Anna', 'Smith', 30),
#     ('Mike', 'Johnson', 40)
# """)
c.execute("""SELECT * FROM persons WHERE last_name = 'Smith'""")
print(c.fetchall())
conn.commit()
conn.close()
