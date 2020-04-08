import sqlite3

con = sqlite3.connect('sample.db')
cObj = con.cursor()

cObj.execute("""CREATE TABLE employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL,
    department TEXT,
    position TEXT
    )""")
con.commit()

cObj.close()
con.close()
