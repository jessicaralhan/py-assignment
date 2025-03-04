import csv
 

with open("appointment.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date", "Time", "Description"])

def schedule_appointment():
    date = input("Enter date(YYYY-MM-DD) -")
    time = input("Enter Time(HH:MM) -")
    description = input("Enter description -")
    
    with open("appointment.csv", "a", newline="") as newfile:
        writer = csv.writer(newfile)
        writer.writerow([date, time, description])


def view_appointment():
        with open("appointment.csv", "r") as file:
            reader = csv.reader(file)
            header = next(reader)  
            appointments = list(reader)

            if not appointments:
                print("No appointments scheduled.")
                return
            
            print("\nScheduled Appointments:")
            for appointment in appointments:
                print(f"Date: {appointment[0]}, Time: {appointment[1]}, Description: {appointment[2]}")
    
while True:
    print("\nSelect an operation:")
    print("1. Schedule appointment")
    print("2. View")

    choice = input("Enter choice - ")
    if choice == '1':
        schedule_appointment()
        print("Appoinment added successfully")
    elif choice == '2':
        view_appointment()



