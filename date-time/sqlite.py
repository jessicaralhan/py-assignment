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
    
def slots_available(appointment_with, date):
    slots = connection_helper("SELECT time FROM appointments WHERE appointment_with = ? AND date = ?", (appointment_with, date))
    available_slots = ["9:30", "10:30", "11:30", "12:30", "14:30", "15:30", "16:30"]

    for slot in slots: 
        available_slots.remove(slot[0])  

    return available_slots

def select_appointment_person():
    appointment_with = None
    while True:
        print("Select who do you want to have an appointment with :")
        print("1. Mr. Jug")
        print("2. Mr Young")
        print("3. Mr Charles")
        print("4. Mr Checo Perez")
        print("5. Mr Hass")
        print("6. Exit")

        choice = input("Choice :")
        if choice == '1':
            appointment_with = "Mr. Jug"
        elif choice == '2':
            appointment_with = "Mr. Young"
        elif choice == '3':
            appointment_with ="Mr Charles"
        elif choice == '4':
            appointment_with = "Mr Checo Perez"
        elif choice == '5':
            appointment_with = "Mr Hass"
        elif choice == '6':
            break
        else:
            print("Invalid choice")
        break
    return appointment_with

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
    appointment_with = select_appointment_person()
    date = input("Enter date (YYYY-MM-DD): ")
    slots = slots_available(appointment_with, date)
      
    while True:  
        print(f"Available slots are {slots} please choose one")
        time = input("Enter time (HH:MM): ")
        if time in slots:
            break
        else:
            print("Slot is not available. Please select one from above -")
           
    error = validate_date_and_time(date,time)
    if error:
        print("cannot proceed further", error)
        return      
    existing_appointment = connection_helper("SELECT * FROM appointments WHERE appointment_with = ? AND time = ? AND date = ?", (appointment_with, time, date))
    if existing_appointment:                                                                      
        available = slots_available(appointment_with, date)
        print("This slot is not available. Available slots are :", available)
        return
    description = input("Enter description: ")
    
    connection_helper("INSERT INTO appointments (name, date, time, description, appointment_with) VALUES (?, ?, ?, ?, ?)", (name, date, time, description, appointment_with))
    print("Appointment added successfully.")

def update_appointments():
    appointment_id = input("Enter appointment id: ")
    appointments = connection_helper("SELECT * FROM appointments WHERE unique_id = ?",(appointment_id))
    print("this is in appointments", appointments)
    if not appointments:
        print("Appointment does not exist")
        return
    up_appointment_with = select_appointment_person()
    user_date = input("Enter new date :")
    slots = slots_available(up_appointment_with, user_date)
      
    while True:  
        print(f"Available slots are {slots} please choose one")
        user_time = input("Enter time (HH:MM): ")
        if user_time in slots:
            break
        else:
            print("Slot is not available. Please select one from above -")

    error = validate_date_and_time(user_date, user_time)
    if error:
        print("Cannot proceed further:", error)
        return
    existing_appointment = connection_helper("SELECT * FROM appointments WHERE appointment_with = ? AND time = ? AND date = ?", (up_appointment_with, user_time, user_date))
    if existing_appointment:  
        available = slots_available(up_appointment_with, user_date) 
        print("This slot is not available. Available slots are :", available)
        return
    new_description = input("Enter new description:")
    connection_helper("UPDATE appointments set appointment_with = ?, date = ?, time = ?, description = ? WHERE unique_id = ?",(up_appointment_with, user_date, user_time, new_description, appointment_id))
    print("updated successfully")
    
    
def view_appointments():
    appointments = connection_helper("SELECT name, date, time, description, appointment_with FROM appointments")
    
    if not appointments:
        print("No appointments scheduled.")
        return
    
    print("Scheduled Appointments:")
    for appointment in appointments:
        print(f"Name: {appointment[0]}, Date: {appointment[1]}, Time: {appointment[2]}, Description: {appointment[3]}, Appointment_with: {appointment[4]}")

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

