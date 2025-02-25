from Database import Database

class DatabaseConnection:

    def __init__(self):
        self.db = Database()
        self.conn = self.db.connect()
        self.cursor = self.conn.cursor()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                dob DATE NOT NULL,
                city VARCHAR(255),
                pincode INT,
                phone_number BIGINT UNIQUE,
                email VARCHAR(255) UNIQUE,
                
            )
        """
