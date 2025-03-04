# py-assigment
**Topic - Data Processing & File Handling**

Problem Statement:
Your company’s application generates log files in the following format:
```log
[2025-02-20 10:15:45] INFO: User logged in
[2025-02-20 10:16:01] ERROR: Database connection failed
[2025-02-20 10:17:23] WARNING: Disk space low
[2025-02-20 10:18:00] DEBUG: File uploaded successfully
[2025-02-20 10:18:00] INFO: File uploaded successfully
```
Write a Python program that:
Reads the log file.
Counts the occurrences of different log levels (INFO, WARNING, ERROR, DEBUG).
Displays a summary like:
```log
INFO: 2
WARNING: 1
ERROR: 1
DEBUG:4
```
**Topic - Automating Repetitive Tasks**

Problem Statement:
Your HR department needs to generate email addresses for new employees based on their names and departments.
Read a CSV file containing new employee details:
```log
Name,Department
John Doe,Sales
Jane Smith,Engineering
Alice Brown,HR
```
Generate email addresses in the format: (firstname.lastname@company.com)
Save the results in a new CSV file.
Expected Output (CSV File):
```log
Name,Department,Email
John Doe,Sales,john.doe@company.com
Jane Smith,Engineering,jane.smith@company.com
Alice Brown,HR,alice.brown@company.com
```

**Topic - Web Scraping & APIs**

Problem Statement:
You need to develop a weather-checking tool that fetches real-time weather information for a given city.
Ask the user to input a city name.
Fetch the weather data from OpenWeatherMap API.
Display:
* Temperature
* Humidity
* Weather Condition (e.g., “Cloudy”, “Sunny”)
Example Output:
```log
Enter city name: Mumbai
Temperature: 30°C
Humidity: 60%
Condition: Clear Sky
```

Save results in 2 files. 
- In a CSV  file with date as today’s date and the value as the output that was received from the API response.  Flatten this data e.g. : 
    28/02/2025 , Mumbai:30C:60%:Clearsky 
    01/03/2025 , Mumbai:27C:90%:Cloudy 
- In a plain text file with the data as shown in the example output. 


**Topic - Simple Database Operations**


Problem Statement:
Create a simple Student Record Management System using SQLite or a CSV file.
Allow users to:
* Add a student record (Name, Roll Number, Marks).
* Update student marks.
* Delete a record.
* Display all records.

Sample Interaction:
```log
1. Add Student
2. Update Marks
3. Delete Student
4. View Students

Enter choice: 1
Enter Name: Alice
Enter Roll Number: 101
Enter Marks: 85
Student added successfully!
```

Implement search functionality.


**Topic - Debugging & Error Handling**

Problem Statement:
The following Python script has errors. Identify and fix them.
```log
def calculate_discount(price, discount):
    discounted_price = price - price * discount / 100
    return discounted_price
print("Enter price: ")
price = input()
print("Enter discount percentage: ")
discount = input()
final_price = calculate_discount(price, discount)
print("Final Price is: " + final_price)
```

Issues:
* input() returns a string, so arithmetic operations will fail.
* The + operator in print("Final Price is: " + final_price) will cause an error.
Fix the script and handle errors gracefully.

**Topic - Working with Dates & Time**

Problem Statement:
Build a simple Appointment Scheduler that:
Allows users to schedule appointments (Date, Time, Description).
Prevents overlapping appointments.
Displays upcoming appointments.
Sample Interaction:
```log
1. Schedule Appointment
2. View Appointments
Enter choice: 1
Enter Date (YYYY-MM-DD): 2025-03-01
Enter Time (HH:MM): 10:00
Enter Description: Doctor's Visit
Appointment added successfully!
```
 Save and retrieve appointments from a file.

**Topic - Mini E-Commerce System**

Problem Statement:
Develop a simple Shopping Cart System where:
Users can add and remove products.
It calculates the total price.
Applies discounts if a discount code is provided.
Example Interaction:
```log
1. Add Product
2. Remove Product
3. View Cart
4. Checkout
Enter choice: 1
Enter Product Name: Laptop
Enter Price: 50000
Product added!
Enter choice: 3
Cart:
- Laptop: ₹50000
Total: ₹50000
Enter choice: 4
Enter Discount Code (if any): SAVE10
Final Price after Discount: ₹45000
```