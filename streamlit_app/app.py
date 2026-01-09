# =========================================
# OLA Ride Insights Dashboard - Streamlit
# =========================================

import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="OLA Ride Insights Dashboard",
    page_icon="🚕",
    layout="wide"
)

st.title("🚕 OLA Ride Insights Dashboard")

# ---------------- MYSQL CONNECTION ----------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="AB12+-@S",      # ✅ your password
        database="ola_ride_insights",
        auth_plugin="mysql_native_password"
    )

@st.cache_data
def load_data():
    conn = get_connection()
    query = "SELECT * FROM ola_rides"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# ---------------- LOAD DATA ----------------
try:
    df = load_data()
    st.success("✅ Connected to MySQL successfully")
except Exception as e:
    st.error(f"MySQL Connection Failed: {e}")
    st.stop()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔎 Filters")

vehicle_filter = st.sidebar.multiselect(
    "Vehicle Type",
    options=df["Vehicle_Type"].dropna().unique(),
    default=df["Vehicle_Type"].dropna().unique()
)

payment_filter = st.sidebar.multiselect(
    "Payment Method",
    options=df["Payment_Method"].dropna().unique(),
    default=df["Payment_Method"].dropna().unique()
)

status_filter = st.sidebar.multiselect(
    "Booking Status",
    options=df["Booking_Status"].dropna().unique(),
    default=df["Booking_Status"].dropna().unique()
)

filtered_df = df[
    (df["Vehicle_Type"].isin(vehicle_filter)) &
    (df["Payment_Method"].isin(payment_filter)) &
    (df["Booking_Status"].isin(status_filter))
]

# ---------------- KPI SECTION ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", len(filtered_df))
col2.metric(
    "Successful Rides",
    len(filtered_df[filtered_df["Booking_Status"] == "Success"])
)
col3.metric(
    "Total Revenue",
    f"{filtered_df[filtered_df['Booking_Status']=='Success']['Booking_Value'].sum():,}"
)
col4.metric(
    "Avg Customer Rating",
    round(filtered_df["Customer_Rating"].mean(), 2)
)

st.divider()

# =====================================================
# QUERY RESULTS (PDF QUESTIONS OUTPUT)
# =====================================================

# Q1 – Successful Bookings
st.subheader("1️⃣ Successful Bookings")
success_df = filtered_df[filtered_df["Booking_Status"] == "Success"]
st.dataframe(success_df[["Booking_ID", "Vehicle_Type", "Booking_Value"]])

# Q2 – Avg Ride Distance per Vehicle Type
st.subheader("2️⃣ Average Ride Distance by Vehicle Type")
avg_distance = (
    filtered_df.groupby("Vehicle_Type")["Ride_Distance"]
    .mean()
    .reset_index()
)
fig2 = px.bar(avg_distance, x="Vehicle_Type", y="Ride_Distance")
st.plotly_chart(fig2, use_container_width=True)

# Q3 – Customer Cancellations
st.subheader("3️⃣ Total Rides Cancelled by Customers")
customer_cancel = filtered_df[
    filtered_df["Canceled_Rides_by_Customer"] != "No"
]
st.metric("Customer Cancelled Rides", len(customer_cancel))

# Q4 – Top 5 Customers by Rides
st.subheader("4️⃣ Top 5 Customers by Total Rides")
top_customers = (
    filtered_df.groupby("Customer_ID")
    .size()
    .reset_index(name="Total_Rides")
    .sort_values("Total_Rides", ascending=False)
    .head(5)
)
st.dataframe(top_customers)

# Q5 – Driver Cancellations (Personal / Car)
st.subheader("5️⃣ Driver Cancellations (Personal / Car Issues)")
driver_cancel = filtered_df[
    filtered_df["Canceled_Rides_by_Driver"].str.contains(
        "Personal|Car", na=False
    )
]
st.metric("Driver Cancelled Rides", len(driver_cancel))

# Q6 – Driver Ratings for Prime Sedan
st.subheader("6️⃣ Driver Ratings (Prime Sedan)")
prime_df = filtered_df[
    (filtered_df["Vehicle_Type"] == "Prime Sedan") &
    (filtered_df["Driver_Ratings"].notna())
]
st.write(
    f"⭐ Max Rating: {prime_df['Driver_Ratings'].max()} | "
    f"Min Rating: {prime_df['Driver_Ratings'].min()}"
)

# Q7 – UPI Payments
st.subheader("7️⃣ Rides Paid Using UPI")
upi_df = filtered_df[filtered_df["Payment_Method"] == "UPI"]
st.dataframe(upi_df[["Booking_ID", "Booking_Value"]])

# Q8 – Avg Customer Rating by Vehicle Type
st.subheader("8️⃣ Average Customer Rating by Vehicle Type")
avg_rating = (
    filtered_df.groupby("Vehicle_Type")["Customer_Rating"]
    .mean()
    .reset_index()
)
fig8 = px.bar(avg_rating, x="Vehicle_Type", y="Customer_Rating")
st.plotly_chart(fig8, use_container_width=True)

# Q9 – Total Successful Booking Value
st.subheader("9️⃣ Total Booking Value (Successful Rides)")
total_value = success_df["Booking_Value"].sum()
st.metric("Total Booking Value", f"{total_value:,}")

# Q10 – Incomplete Rides
st.subheader("🔟 Incomplete Rides with Reason")
incomplete_df = filtered_df[filtered_df["Incomplete_Rides"] == "Yes"]
st.dataframe(incomplete_df[["Booking_ID", "Incomplete_Rides_Reason"]])

st.divider()
st.caption("📌 SQL executed in MySQL | Results shown via Streamlit UI")
