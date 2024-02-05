
import mysql.connector
from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            db_properties = DBPropertyUtil.get_db_properties()
            connection = mysql.connector.connect(**db_properties)
            if connection.is_connected():
                print("Connected to the database")
            return connection

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            raise e
