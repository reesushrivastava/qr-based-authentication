import mysql.connector
from mysql.connector import Error
 
def init_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',       
            user='root',            
            password='6395',    
            database='qrcode_db'    
        )
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS qr_codes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                unique_id VARCHAR(255) UNIQUE NOT NULL,
                name VARCHAR(255),
                age INT,
                mobile_number BIGINT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

def save_to_db(unique_id, name=None, age=None, mobile_number=None):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='6395',
            database='qrcode_db'
        )
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO qr_codes (unique_id, name, age, mobile_number)
            VALUES (%s, %s, %s, %s)
        ''', (unique_id, name, age, mobile_number))
        conn.commit()
        conn.close()
        print("Data saved to database successfully.")
    except Error as e:
        print(f"Error saving data to MySQL: {e}")

def update_to_db(unique_id, name, age, mobile_number):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='6395',
            database='qrcode_db'
        )
        cursor = conn.cursor()
        # Correcting the SQL query for UPDATE
        cursor.execute('''
            UPDATE qr_codes
            SET name = %s, age = %s, mobile_number = %s
            WHERE unique_id = %s
        ''', (name, age, mobile_number, unique_id))
        
        conn.commit()
        print("Data updated in database successfully.")
    except Error as e:
        print(f"Error updating data in MySQL: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def fetch_from_db(unique_id):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='6395',
            database='qrcode_db'
        )
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM qr_codes WHERE unique_id = %s
        ''', (unique_id,))
        result = cursor.fetchone()
        conn.close()
        return result
    except Error as e:
        print(f"Error fetching data from MySQL: {e}")
        return None
