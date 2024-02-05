
from configparser import ConfigParser
from connectionutil import DBConnection


class DBPropertyUtil:
    @staticmethod
    def get_db_properties():
        config = ConfigParser()
        config.read('database_config.ini')
        return {
            'host': config.get('database', 'host'),
            'user': config.get('database', 'user'),
            'password': config.get('database', 'password'),
            'database': config.get('database', 'database'),
            'port': config.getint('database', 'port'),
        }
