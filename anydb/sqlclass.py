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
        return self.cursor.execute(f'SELECT * FROM {table_name}')

    def insert_data(self, table_name, data):
        statement = f'INSERT INTO {table_name} VALUES {data}'
        self.cursor.execute(statement)
        self.conn.commit()

    def update_data(self, table_name, data):
        self.descriptions = [description[0] for description in self.get_all_data(self.table).description]
        update_string = ''
        Q = '"'
        for i,j in zip(self.descriptions[1:], data[1:]):
            if i == self.descriptions[-1]:
                update_string += (i + '=' + Q + j + Q)
            else:
                update_string += (i + '=' + Q + j + Q +', ')
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
    
    #app.delete_data(app.table, ('25', 'SoSo', '97000.0', 'Time', 'Viewer'))
    
    all = app.get_all_data(app.table)
    print(app.print_data(all))
