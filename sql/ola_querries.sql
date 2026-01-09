CREATE DATABASE ola_ride_insights;
USE ola_ride_insights;

CREATE TABLE ola_rides (
    Date DATE,
    Time TIME,
    Booking_ID VARCHAR(50),
    Booking_Status VARCHAR(50),
    Customer_ID VARCHAR(50),
    Vehicle_Type VARCHAR(50),
    Pickup_Location VARCHAR(100),
    Drop_Location VARCHAR(100),
    V_TAT FLOAT,
    C_TAT FLOAT,
    Canceled_Rides_by_Customer VARCHAR(100),
    Canceled_Rides_by_Driver VARCHAR(100),
    Incomplete_Rides VARCHAR(10),
    Incomplete_Rides_Reason VARCHAR(100),
    Booking_Value INT,
    Payment_Method VARCHAR(50),
    Ride_Distance INT,
    Driver_Ratings FLOAT,
    Customer_Rating FLOAT,
    Vehicle_Images TEXT
);


SET GLOBAL local_infile = 1;

# Q1. Retrieve all successful bookings
SELECT *
FROM ola_rides
WHERE Booking_Status = 'Success';

# Q2. Average ride distance for each vehicle type
SELECT 
    Vehicle_Type,
    AVG(Ride_Distance) AS avg_ride_distance
FROM ola_rides
GROUP BY Vehicle_Type;

# Q3. Total number of rides cancelled by customers
SELECT 
    COUNT(*) AS total_customer_cancellations
FROM ola_rides
WHERE Canceled_Rides_by_Customer <> 'No';

# Q4. Top 5 customers who booked highest number of rides
SELECT 
    Customer_ID,
    COUNT(*) AS total_rides
FROM ola_rides
GROUP BY Customer_ID
ORDER BY total_rides DESC
LIMIT 5;

# Q5. Rides cancelled by drivers due to personal & car-related issues
SELECT 
    COUNT(*) AS driver_cancelled_rides
FROM ola_rides
WHERE Canceled_Rides_by_Driver LIKE '%Personal%'
   OR Canceled_Rides_by_Driver LIKE '%Car%';

# Q6. Max & Min driver ratings for Prime Sedan bookings
SELECT 
    MAX(Driver_Ratings) AS max_rating,
    MIN(Driver_Ratings) AS min_rating
FROM ola_rides
WHERE Vehicle_Type = 'Prime Sedan'
  AND Driver_Ratings IS NOT NULL;

# Q7. Retrieve all rides paid using UPI
SELECT *
FROM ola_rides
WHERE Payment_Method = 'UPI';

# Q8. Average customer rating per vehicle type
SELECT 
    Vehicle_Type,
    AVG(Customer_Rating) AS avg_customer_rating
FROM ola_rides
WHERE Customer_Rating IS NOT NULL
GROUP BY Vehicle_Type;

# Q9. Total booking value of successfully completed rides
SELECT 
    SUM(Booking_Value) AS total_successful_booking_value
FROM ola_rides
WHERE Booking_Status = 'Success';

# Q10. List all incomplete rides with reason
SELECT 
    Booking_ID,
    Incomplete_Rides_Reason
FROM ola_rides
WHERE Incomplete_Rides = 'Yes';


