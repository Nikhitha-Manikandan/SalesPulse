
from database import get_connection

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
