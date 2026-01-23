# 🚕 OLA Ride Insights Dashboard

An end-to-end Data Analytics project that analyzes OLA ride data using MySQL and presents insights through an interactive Streamlit dashboard.  
This project fulfills both **mentor guidance** and **PDF requirements** by combining SQL query analysis with a user-friendly UI.

---

## 📌 Project Objective

- Store and manage ride data in **MySQL**
- Solve business questions using **SQL queries**
- Connect MySQL with **Streamlit**
- Display **SQL query results interactively**
- Allow users to explore data using filters

---

## 🛠 Tech Stack

- MySQL (Database)
- Python
- Pandas
- Streamlit
- Plotly
- Power BI (for separate dashboard)

---

## 📂 Project Structure

  OLA-Ride-Insights/
  │
  data/
   ├── raw/
   │    └── OLA_DataSet.xlsx
   └── processed/
        └── ola_cleaned.csv
  
  docs/
   └── insights.md
  
  notebooks/
   ├── 01_data_understanding.ipynb
   ├── 02_data_cleaning.ipynb
   └── 03_eda.ipynb
  
  powerbi/
   └── OLA Ride Insights Dashboard.pbix
  
  sql/
   └── ola_queries.sql
  
  streamlit_app/
   ├── app.py
   └── requirements.txt
  
  README.md




---

## 🗄 Database Details

**Database Name:** `ola_ride_insights`  
**Table Name:** `ola_rides`

### Important Columns
- Booking_ID
- Booking_Status
- Vehicle_Type
- Booking_Value
- Payment_Method
- Ride_Distance
- Driver_Ratings
- Customer_Rating

---

## 📊 SQL Queries Implemented

The following analytical queries were executed in MySQL and their **results are displayed in the Streamlit app**:

1. Retrieve all successful bookings  
2. Average ride distance per vehicle type  
3. Total rides cancelled by customers  
4. Top 5 customers by number of rides  
5. Driver cancellations (personal / car related)  
6. Maximum & minimum driver ratings (Prime Sedan)  
7. Rides paid using UPI  
8. Average customer rating per vehicle type  
9. Total booking value of successful rides  
10. Incomplete rides with reasons  

> ⚠️ SQL queries are **not shown in the UI**, only their **results**, as required by the project PDF.

---

## 🖥 Streamlit Application Features

### 🔹 Sidebar Filters
- Vehicle Type
- Payment Method
- Booking Status

### 🔹 KPI Metrics
- Total Rides
- Successful Rides
- Total Revenue
- Average Customer Rating

### 🔹 Visualizations
- Total Rides by Vehicle Type
- Total Revenue by Vehicle Type
- Interactive charts using Plotly
- Query result tables

---

## 🚀 How to Run the Project

### Step 1: Clone Repository

git clone https://github.com/your-username/OLA-Ride-Insights.git
cd OLA-Ride-Insights/streamlit_app

# Step 2: Install Dependencies
# Run the following command to install all required Python packages
pip install -r requirements.txt

# Step 3: Setup MySQL
# - Create database: ola_ride_insights
# - Create table: ola_rides
# - Insert the dataset into the table
# - Update MySQL credentials (username, password, database) in app.py

# Step 4: Run Streamlit Application
# Start the Streamlit dashboard using the command below
streamlit run app.py


# ===============================
# Key Learnings
# ===============================

# - Writing real-world SQL queries for business problems
# - Connecting MySQL database with Streamlit
# - Building interactive dashboards with filters and KPIs
# - Displaying SQL query results in a user-friendly UI
# - Presenting insights in a professional and industry-ready manner


# ===============================
# Conclusion
# ===============================

# This project demonstrates:
# - SQL query execution and analysis using MySQL
# - Seamless integration of MySQL with Streamlit
# - Interactive data visualization and filtering
# - Industry-level dashboard design

# The project fully satisfies mentor expectations
# and follows all requirements mentioned in the project PDF.


# ===============================
# Author
# ===============================

# Name: Sibam Sen
# Degree: Final Year B.Tech (ECE)
# Domain: Data Analytics & Visualization

