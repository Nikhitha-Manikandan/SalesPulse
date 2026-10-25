import streamlit as st
import pandas as pd
from products import get_products
from analytics import get_total_revenue, get_total_orders,get_total_customers,get_low_stock_products,get_sales_by_products,get_order_status_summary,get_customer_order_summary

st.set_page_config(
    page_title="SalesPulse | Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background-color: #F5F7FB;
    }

    h1 {
        color: #172554;
        font-weight: 750;
        letter-spacing: -1px;
    }

    h2, h3 {
        color: #1E293B;
        font-weight: 650;
    }

    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #E2E8F0;
        padding: 22px 20px;
        border-radius: 14px;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
    }

    [data-testid="stMetricLabel"] {
        color: #64748B;
        font-size: 14px;
    }

    [data-testid="stMetricValue"] {
        color: #1D4ED8;
        font-weight: 700;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        overflow: hidden;
    }

    hr {
        border-color: #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)


st.title("SalesPulse")
st.caption("Sales Management & Business Analytics Dashboard")
st.divider()

total_revenue = get_total_revenue()
total_orders = get_total_orders()
total_customers = get_total_customers()

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)

st.subheader("Low-Stock Products")
low_stock_products = get_low_stock_products()

if low_stock_products:
    st.dataframe(
        low_stock_products,
        column_config={
            0: "Product Name",
            1: "Stock Quantity"
        },
        hide_index=True
    )
else:
    st.success("All products are sufficiently stocked!")
st.subheader("Product Inventory")

products = get_products()

st.dataframe(
    products,
    column_config={
        0: "Product ID",
        1: "Product Name",
        2: "Price",
        3: "Stock Quantity"
    },
    hide_index=True
)
st.subheader("Sales by Product")

sales = get_sales_by_products()

sales_df = pd.DataFrame(
    sales,
    columns=["Product Name", "Total Revenue"]
)

st.dataframe(
    sales_df,
    column_config={
        "Product Name": "Product Name",
        "Total Revenue": st.column_config.NumberColumn(
            "Total Revenue (₹)",
            format="₹%.2f"
        )
    },
    hide_index=True,
    use_container_width=True
)
st.subheader("Revenue by Product")

st.bar_chart(
    sales_df,
    x="Product Name",
    y="Total Revenue"
)
st.subheader("Order Status Analysis")

order_status = get_order_status_summary()

status_df = pd.DataFrame(
    order_status,
    columns=["Order Status", "Number of Orders"]
)

st.dataframe(status_df, hide_index=True)

st.bar_chart(
    status_df,
    x="Order Status",
    y="Number of Orders"
)


st.subheader("Customer Order Analysis")

customer_data = get_customer_order_summary()

customer_df = pd.DataFrame(
    customer_data,
    columns=["Customer Name", "City", "Total Orders"]
)

st.dataframe(
    customer_df,
    hide_index=True,
    use_container_width=True
)

st.bar_chart(
    customer_df,
    x="Customer Name",
    y="Total Orders"
)
