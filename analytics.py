
from database import get_connection

def get_total_revenue():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(quantity*unit_price) FROM order_items;")
    result = cursor.fetchone()
    total_revenue= result[0]

    cursor.close()
    conn.close()

    return total_revenue


def get_total_orders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(order_id) FROM orders;")
    result = cursor.fetchone()
    total_orders= result[0]

    cursor.close()
    conn.close()

    return total_orders

def get_low_stock_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT product_name,stock_quantity FROM products WHERE stock_quantity < 10;")
    low_stock_products= cursor.fetchall()
    
    cursor.close()
    conn.close()

    return low_stock_products

def get_sales_by_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT p.product_name,SUM(o.quantity*o.unit_price) as total_revenue FROM products as p INNER JOIN order_items as o on p.product_id=o.product_id GROUP BY p.product_id,p.product_name;")
    sales_by_products= cursor.fetchall()
    
    cursor.close()
    conn.close()

    return sales_by_products

def get_order_status_summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status, COUNT(order_id) AS total_orders
        FROM orders
        GROUP BY status;
    """)

    order_status = cursor.fetchall()

    cursor.close()
    conn.close()

    return order_status

def get_customer_order_summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            c.name,
            c.city,
            COUNT(o.order_id) AS total_orders
        FROM customers AS c
        LEFT JOIN orders AS o
            ON c.customer_id = o.customer_id
        GROUP BY c.customer_id, c.name, c.city
        ORDER BY total_orders DESC;
    """)

    customer_summary = cursor.fetchall()

    cursor.close()
    conn.close()

    return customer_summary

def get_total_customers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM customers")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result[0]


if __name__ == "__main__":
        print("Total Revenue:", get_total_revenue())
        print("Total Orders:",get_total_orders())
        print("Total low stock quantity:",get_low_stock_products())
        print("Sales by Product:", get_sales_by_products())
        print("Order Status Summary:", get_order_status_summary())