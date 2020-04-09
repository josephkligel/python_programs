import sqlite3

conn = sqlite3.connect('/home/jkligel/backups/transactions.db')
c = conn.cursor()

c.execute("""CREATE TABLE budget2020(
id INTEGER PRIMARY KEY,

)""")
