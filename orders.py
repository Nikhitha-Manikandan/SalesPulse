from database import get_connection

def get_orders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    cursor.close()
    conn.close()

    return orders

if __name__ == "__main__":
    for order in get_orders():
        print(order)