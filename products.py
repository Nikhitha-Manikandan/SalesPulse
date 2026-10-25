
from database import get_connection

def get_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products ")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products

if __name__ == "__main__":
    for product in get_products():
        print(product)
