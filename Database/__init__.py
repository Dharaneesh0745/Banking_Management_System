import mysql.connector
from Config import DB_CONFIG

class Database:

    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(**DB_CONFIG)
            except ConnectionError:
                print("Error connection to database")
        return self.connection

    def close(self):
        if self.connection:
            self.connect().close()
            self.connection = None
