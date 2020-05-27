import sqlite3

conn = sqlite3.Connection('star_ships.db')
cursor = conn.cursor()

table_statement = """CREATE TABLE IF NOT EXISTS ships(
id INTEGER PRIMARY KEY NOT NULL, 
name TEXT NOT NULL,
captain NOT NULL,
size REAL,
crew_size REAL,
description LONG
)"""

cursor.execute(table_statement)
conn.commit()

cursor.close()
conn.close()
