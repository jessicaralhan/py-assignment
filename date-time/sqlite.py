import sqlite3
from datetime import datetime
import datetime 


# 1) Validations for all fields when we are creating an appointment. 
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def validate_time(time_str):
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False
# open the connection 
# any operation (update, create, select, delete) 
# commit and close the connection 
def connection_helper(statement, params = ()):
    print("statement is ", statement)
    print("params are", params)
    conn = sqlite3.connect("appointments.db")

    cursor = conn.cursor()
    try:
        cursor.execute(statement, params)
        conn.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
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
    date = "2020-12-20" #input("Enter date (YYYY-MM-DD): ")
    time = "19:30" #input("Enter time (HH:MM): ")
    existing_appointment = connection_helper("SELECT * FROM appointments WHERE time = ? AND date = ?", (time, date))
    print(existing_appointment)
    if existing_appointment:
        print("not availble")
        return
    description = input("Enter description: ")
    appointment_with = input("Who do you have an appointment with : ")
    
    
    connection_helper("INSERT INTO appointments (name, date, time, description, appointment_with) VALUES (?, ?, ?, ?, ?)", (name, date, time, description, appointment_with))
    
    print("Appointment added successfully.")

  
def update_appointments():
    current_date = datetime.datetime.now()
    print(current_date)
    appointment_id = input("Enter appointment id: ")
    # appointments = connection_helper("SELECT * FROM appointments WHERE unique_id = ?",(appointment_id))
    # if appointment_id not in appointments:
    #     print("not exist")
    #     return
    #user_date = "2025-3-13 12:30"
    user_date = input("Enter new date :")  # "2025-3-14"
    user_time = input("Enter new time :")  # "13:30"
    # 
    user_date_time = datetime.datetime.strptime(user_date + user_time, "%Y-%m-%d%H:%M")
    if user_date_time > current_date:
        print("user date is greater than current date so should be added")
    else:
        print("should not be added")
        return
    
    new_description = input("Enter new description:")
    connection_helper("UPDATE appointments set date = ?, time = ?, description = ? WHERE unique_id = ?",(user_date, user_time, new_description, appointment_id))
    print("updated successfully")

    
def view_appointments():
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, date, time, description FROM appointments")
    appointments = cursor.fetchall()
    conn.close()
    
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

