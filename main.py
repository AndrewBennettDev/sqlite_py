import sqlite3

class DatabaseHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    value INTEGER
                )
            ''')
            self.conn.commit()
        except Exception as e:
            print(f"Error creating table: {e}")

    def add_data(self, name, value):
        try:
            self.cursor.execute('''
                INSERT INTO data (name, value)
                VALUES (?, ?)
            ''', (name, value))
            self.conn.commit()
        except Exception as e:
            print(f"Error adding data: {e}")

    def get_data(self, data_id):
        try:
            self.cursor.execute('''
                SELECT * FROM data WHERE id=?
            ''', (data_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error getting data: {e}")

    def update_data(self, data_id, new_name, new_value):
        try:
            self.cursor.execute('''
                UPDATE data SET name=?, value=? WHERE id=?
            ''', (new_name, new_value, data_id))
            self.conn.commit()
        except Exception as e:
            print(f"Error updating data: {e}")

    def delete_data(self, data_id):
        """Delete a record from the database by ID."""
        try:
            self.cursor.execute('''
                DELETE FROM data WHERE id=?
            ''', (data_id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error deleting data: {e}")

    def close_connection(self):
        self.conn.close()



db_handler = DatabaseHandler('example.db')

db_handler.add_data('Record 1', 42)

record = db_handler.get_data(1)
print("Retrieved Record:", record)

db_handler.update_data(1, 'Updated Record', 99)

updated_record = db_handler.get_data(1)
print("Updated Record:", updated_record)

db_handler.delete_data(1)

db_handler.close_connection()
