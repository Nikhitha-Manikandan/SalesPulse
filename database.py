
import mysql.connector


import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "salespulse")
    )
    return conn

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nikhil1@34",
        database="salespulse"
    )

def get_customers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return customers

if __name__ == "__main__":
    for customer in get_customers():
        print(customer)
