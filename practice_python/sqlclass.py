import sqlite3

class Person():
    def __init__(self, first=None, last=None, age=None):
        self.first = first
        self.last = last
        self.age = age

    def clone_person(self, result):
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("""
    SELECT * FROM persons WHERE last_name = 'Smith'
""")
person = Person()
person.clone_person(c.fetchone())
print(person.first, person.last, person.age, sep='\n')

# person2 = Person('Bob', 'Davis', 23)
# c.execute(f"""INSERT INTO persons VALUES('{person2.first}', '{person2.last}', '{person2.age}')""")
# conn.commit()
person3 = Person('Lisa', 'Kudrow', 45)
c.execute("INSERT INTO persons VALUES(?, ?, ?)", (person3.first, person3.last, person3.age))
conn.commit()

c.execute('SELECT * FROM persons')
print(c.fetchall())
conn.close()
