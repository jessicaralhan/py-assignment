import sqlite3
import datetime
from dateutil.parser import parser
from datetime import datetime as dt
 
def validate_date_and_time(date, time):
    # 1) Date should be a valid calender date
    try:
        dt.strptime(date, '%Y-%m-%d')  # Validate date format
    except ValueError as e:
        return str(e)
    # 2) Time should be valid 
    try:
        dt.strptime(time, '%H:%M') # Valid Time format
    except ValueError as e:
        return str(e)
    # 3) Date should be greater than current date 
    current_date = datetime.datetime.now()
    user_date_time = datetime.datetime.strptime(date + time, "%Y-%m-%d%H:%M")  
    if user_date_time > current_date:  
        return None  
    else:
        return "Date should be a future date"  

# open the connection 
# any operation (update, create, select, delete) 
# commit and close the connection 
def connection_helper(statement, params = ()):
    conn = sqlite3.connect("appointments.db")

    cursor = conn.cursor()
    try:
        cursor.execute(statement, params)
        conn.commit()
    except sqlite3.Error as er:
        return 
    if "SELECT" in statement:
        return cursor.fetchall()
    conn.close()

    return

def create_table():
    connection_helper('''CREATE TABLE IF NOT EXISTS appointments (
                        unique_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        date TEXT,
                        time TEXT,
                        description TEXT,
                        appointment_with TEXT )''')
 
def schedule_appointment():
    name = input("Enter name : ")
    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM): ")                                                                  

    error = validate_date_and_time(date,time)
    if error:
        print("cannot proceed further", error)
        return      
    existing_appointment = connection_helper("SELECT * FROM appointments WHERE time = ? AND date = ?", (time, date))
    if existing_appointment:                                                                      
        print("not availble")
        return
    description = input("Enter description: ")
    appointment_with = input("Who do you have an appointment with : ")
    
    connection_helper("INSERT INTO appointments (name, date, time, description, appointment_with) VALUES (?, ?, ?, ?, ?)", (name, date, time, description, appointment_with))
    print("Appointment added successfully.")

def update_appointments():
    appointment_id = input("Enter appointment id: ")
    appointments = connection_helper("SELECT * FROM appointments WHERE unique_id = ?",(appointment_id))
    if appointments:
        print("Appointment does not exist")
        return
    user_date = input("Enter new date :")
    user_time = input("Enter new time :")
    error = validate_date_and_time(user_date, user_time)
    if error:
        print("Cannot proceed further:", error)
        return
    
    new_description = input("Enter new description:")
    connection_helper("UPDATE appointments set date = ?, time = ?, description = ? WHERE unique_id = ?",(user_date, user_time, new_description, appointment_id))
    print("updated successfully")

    
def view_appointments():
    appointments = connection_helper("SELECT name, date, time, description FROM appointments")
    
    if not appointments:
        print("No appointments scheduled.")
        return
    
    print("Scheduled Appointments:")
    for appointment in appointments:
        print(f"Name: {appointment[0]}, Date: {appointment[1]}, Time: {appointment[2]}, Description: {appointment[3]}")

def main():
    create_table()
    while True:
        print("\nSelect an operation:")
        print("1. Schedule appointment")
        print("2. Update appointments")
        print("3. View appointments")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        if choice == '1':
            schedule_appointment()
        elif choice == '2':
            update_appointments()
        elif choice == '3':
            view_appointments()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

