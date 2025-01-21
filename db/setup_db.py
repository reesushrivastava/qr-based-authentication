import mysql.connector

# Database setup
def init_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="6395",  # Replace with your MySQL password
        database="qrcode_db"
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS QRCodeData (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Function to save data to the database
def save_to_db(data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="6395",  
        database="qrcode_db"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO QRCodeData (data) VALUES (%s)", (data,))
    conn.commit()
    conn.close()
