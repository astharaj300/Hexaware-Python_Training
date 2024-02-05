import mysql.connector


class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ABcd300#$",
            database="techshop"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
