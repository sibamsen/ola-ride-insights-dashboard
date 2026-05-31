# 🚕 OLA Ride Insights Dashboard

An end-to-end Data Analytics and Business Intelligence project that transforms raw ride-hailing data into actionable business insights through data cleaning, SQL analytics, interactive dashboards, and KPI reporting.

## 📌 Project Overview

The OLA Ride Insights Dashboard is designed to analyze ride-booking operations, identify business bottlenecks, and monitor key performance indicators (KPIs) using Python, MySQL, Streamlit, and Power BI.

The project processes over **103,000 ride records**, performs data cleaning and transformation, stores the data in a relational database, executes business-critical SQL analyses, and presents insights through interactive dashboards.

---

## 🎯 Business Problem

Ride-hailing platforms generate massive volumes of operational data. However, raw booking files often contain:

* Missing values
* Inconsistent records
* Limited reporting capabilities
* Lack of centralized KPI monitoring

This project addresses these challenges by creating a complete analytics pipeline that enables stakeholders to monitor ride performance, revenue trends, customer behavior, and cancellation patterns.

---

## 🛠 Tech Stack

### Programming & Analytics

* Python
* Pandas
* NumPy

### Database

* MySQL

### Visualization

* Power BI
* Plotly Express

### Dashboarding

* Streamlit

### Development Tools

* Git
* GitHub
* Jupyter Notebook
* VS Code

---

## 📂 Project Structure

```text
OLA-Ride-Insights/
│
├── data/
│   ├── raw/
│   │   └── OLA_DataSet.xlsx
│   └── processed/
│       └── ola_cleaned.csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_eda.ipynb
│
├── sql/
│   └── ola_queries.sql
│
├── streamlit_app/
│   ├── app.py
│   └── requirements.txt
│
└── powerbi/
    └── OLA Ride Insights Dashboard.pbix
```

## 🧹 Data Preprocessing

The dataset containing **103,024 ride records** was cleaned and transformed using Python and Pandas.

### Data Cleaning Steps

* Imputed missing customer cancellation values
* Imputed missing driver cancellation values
* Handled incomplete ride information
* Preserved rating null values for cancelled rides
* Filled missing payment methods
* Created temporal features:

  * Ride Day
  * Ride Month
  * Ride Hour
* Exported cleaned data for database migration

---

## 🗄 Database Design

The cleaned dataset was migrated to MySQL and stored in the `ola_rides` table.

### Key Attributes

* Booking Status
* Vehicle Type
* Pickup & Drop Locations
* Booking Value
* Ride Distance
* Payment Method
* Driver Rating
* Customer Rating
* Cancellation Reasons

---

## 📊 SQL Analytics Performed

The project includes analytical SQL queries to answer business-critical questions:

1. Retrieve all successful bookings
2. Calculate average ride distance by vehicle type
3. Count rides cancelled by customers
4. Identify top customers by booking volume
5. Analyze driver cancellation reasons
6. Find rating extremes for Prime Sedan rides
7. Retrieve UPI transactions
8. Calculate average customer ratings
9. Compute total successful booking revenue
10. Analyze incomplete rides and associated reasons

---

## 📈 Key Business Insights

### Operational Metrics

| Metric                 | Value   |
| ---------------------- | ------- |
| Total Bookings         | 103,024 |
| Successful Rides       | 63,967  |
| Completion Rate        | 62.1%   |
| Customer Cancellations | 10,499  |
| Driver Cancellations   | 18,434  |
| Driver Not Found       | 10,124  |

### Revenue Metrics

| Metric                  | Value          |
| ----------------------- | -------------- |
| Total Revenue           | ₹35.08 Million |
| Average Customer Rating | 4.0 / 5.0      |

### Business Findings

* Customer cancellations were significantly lower than total operational disruptions caused by driver-side issues.
* Driver availability constraints resulted in over 10,000 "Driver Not Found" incidents.
* Prime Sedan rides achieved the highest average ride distances.
* Cash and UPI dominated transaction volumes.
* Revenue exceeded ₹35 million across successful ride bookings.

---

## 🖥 Streamlit Dashboard Features

### Interactive Filters

* Vehicle Type
* Payment Method
* Booking Status

### KPI Cards

* Total Rides
* Successful Rides
* Total Revenue
* Average Customer Rating

### Visualizations

* Average Ride Distance by Vehicle Type
* Average Customer Rating by Vehicle Type
* Interactive Query Outputs
* Dynamic Business Metrics

---

## 📊 Power BI Dashboard

The Power BI dashboard provides executive-level reporting with:

* Revenue Analysis
* Ride Status Monitoring
* Cancellation Trends
* Vehicle Performance Analysis
* Customer Satisfaction Tracking
* Interactive KPI Visualizations

---

## 🚀 Outcomes

* Processed and analyzed 103K+ ride records.
* Built an end-to-end analytics pipeline using Python and MySQL.
* Generated actionable insights from operational ride data.
* Developed interactive dashboards using Streamlit and Power BI.
* Enabled data-driven decision-making through KPI monitoring and business intelligence reporting.

---

## 👨‍💻 Author

**Sibam Sen**
