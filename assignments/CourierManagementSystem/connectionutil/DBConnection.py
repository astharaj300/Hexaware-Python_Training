
import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                config = ConfigParser()
                config.read('database_config.ini')

                db_config = {
                    'host': config.get('database', 'host'),
                    'user': config.get('database', 'user'),
                    'password': config.get('database', 'password'),
                    'database': config.get('database', 'database'),
                    'port': config.getint('database', 'port'),
                }

                DBConnection.connection = mysql.connector.connect(**db_config)

                if DBConnection.connection.is_connected():
                    print("Connected to the database")

            except Error as e:
                print(f"Error: {e}")
                raise e

        return DBConnection.connection
