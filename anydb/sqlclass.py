import sqlite3

class Database():
    def __init__(self, database_name, table=None):
        self.database_name = database_name
        self.table = table
        self.connect_to_db()
        self.tables = self.get_tables()

    def connect_to_db(self):
        self.conn = sqlite3.Connection(self.database_name)
        self.cursor = self.conn.cursor()

    def get_tables(self):
        return list(self.cursor.execute('SELECT name FROM sqlite_master WHERE type="table";'))

    def get_all_data(self, table_name):
        self.all = self.cursor.execute(f'SELECT * FROM {table_name}')
        self.descriptions = [description[0] for description in self.all.description]
        return self.all

    def insert_data(self, table_name, data):
        data = tuple(data) #Insert statement have to use tuples
        statement = f'INSERT INTO {table_name} VALUES {data}'
        self.cursor.execute(statement)
        self.conn.commit()

    def update_data(self, table_name, data):
        update_string = ''
        for i,j in zip(self.descriptions[1:], data[1:]):
            if i == self.descriptions[-1]:
                update_string += f'{i}="{j}"'
            else:
                update_string += f'{i}="{j}", '
        statement = f'UPDATE {table_name} SET {update_string} WHERE {self.descriptions[0]}={data[0]}'
        self.cursor.execute(statement)
        self.conn.commit()

    def delete_data(self, table_name, data):
        statement = f'DELETE FROM {table_name} WHERE {self.descriptions[0]}={data[0]}'
        self.cursor.execute(statement)
        self.conn.commit()

    def print_data(self, data):
        for i in data:
         print(i)

if __name__ == '__main__':
    app = Database('sample.db', table='employees')
    app.insert_data(app.table, ('11', 'Sonya', '100000.0', 'MK', 'Agent'))
    all = app.get_all_data(app.table)
    print(app.print_data(all))
