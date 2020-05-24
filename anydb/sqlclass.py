import sqlite3
import collections

class Database():
    def __init__(self, database_name, table=None):
        self.database_name = database_name
        self.table = table
        self.connect_to_db()

    def connect_to_db(self):
        self.conn = sqlite3.Connection(self.database_name)
        self.cursor = self.conn.cursor()

    def get_all_data(self, table_name):
        return self.cursor.execute(f'SELECT * FROM {table_name}')

    def insert_data(self, table_name, data):
        statement = f'INSERT INTO {table_name} VALUES {data}'
        self.cursor.execute(statement)
        self.conn.commit()

    def update_data(self, table_name, data):
        descriptions = [description[0] for description in self.get_all_data(self.table).description]
        update_dict = collections.OrderedDict()
        for i,j in zip(descriptions[1:], data[1:]):
            update_dict[i] = j            
        statement = f'UPDATE {table_name} SET {update_dict} WHERE {descriptions[0]}={data[0]}'
        self.cursor.execute(statement)
        self.conn.commit()

    def delete_data(self, data=(), table_name=None):
        pass

    def print_data(self, data):
        for i in data:
         print(i)

if __name__ == '__main__':
    app = Database('sample.db', table='employees')
    
    app.update_data(app.table, (25, 'SoSo', 97000.0, 'Time', 'Viewer'))
    
    all = app.get_all_data(app.table)
    print(app.print_data(all))
