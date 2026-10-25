# SalesPulse — Sales Management & Business Analytics Dashboard

SalesPulse is a Python-based sales analytics dashboard that connects to a MySQL database and visualizes sales performance, product inventory, order statuses, and customer activity using Streamlit.

## Features

- **Sales Overview:** Displays total revenue, total orders, and total customers.
- **Product Inventory:** Displays product details and stock quantities.
- **Sales by Product:** Analyzes product-wise revenue using tables and charts.
- **Order Status Analysis:** Summarizes orders by status.
- **Customer Order Analysis:** Shows customer-wise order counts.
- **Low-Stock Monitoring:** Identifies products requiring stock attention.

## Tech Stack

- Python
- MySQL
- Streamlit
- Pandas
- mysql-connector-python
- python-dotenv

## Project Structure

```text
SalesPulse/
├── app.py
├── database.py
├── analytics.py
├── products.py
├── customers.py
├── orders.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

1. Install Python and MySQL.
2. Clone or download this repository.
3. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create a MySQL database named `salespulse` and configure the required tables.
5. Create a `.env` file in the project root with your local database credentials:

   ```dotenv
   DB_HOST=localhost
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=salespulse
   ```

6. Ensure `.env` is excluded in `.gitignore`.
7. Run the dashboard:

   ```bash
   python -m streamlit run app.py
   ```

8. Open the local URL displayed in the terminal.

## Security

Database credentials are stored in environment variables rather than being included directly in the application code. Never commit your `.env` file or publish database passwords.

## Future Improvements

- Add and manage customers, products, and orders through the dashboard.
- Add date-range filters and sales trend analysis.
- Export analytical reports.
- Deploy the dashboard online.

## Author

Developed as a Python, SQL, and data analytics portfolio project.
