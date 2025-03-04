import csv 


with open("record_managemnet.csv", "w", newline='') as csvfile:
    writer= csv.writer(csvfile)
    writer.writerow(["Name ", "Roll no. ", "Marks"])

def add_student():
    name = input("enter name -")
    roll_no = input("enter roll no. -")
    marks = input("enter marks -")

    with open("record_managemnet.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, roll_no, marks])


def update_marks():
    roll_no = input("enter roll no. ")
    new_marks = input("enter marks")
    rows = []
    updated = False

    with open("record_managemnet.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[1] == roll_no:
                row[2] = new_marks
                updated = True
            rows.append(row)
    if updated:
        with open("record_managemnet.csv", "w", newline='') as file:
            writer= csv.writer(file)
            writer.writerows(rows)
        print("updated")
    else:
        print("not updated")

def delete_student():
    roll_no = input("enter roll no. ")
    rows = []
    deleted = False
    with open("record_managemnet.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[1] != roll_no:
                rows.append(row)
            else:
                deleted = True
    if deleted:
        with open("record_managemnet.csv", "w", newline='') as file:
            writer= csv.writer(file)
            writer.writerow(rows)
        print("deleted")
    else:
        print("not deleted")
            
def view_student():
    with open("record_managemnet.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


while True:
    print("\nSelect an operation:")
    print("1. Add Student")
    print("2. Update marks")
    print("3. Delete Student")
    print("4. View Students")

    choice = input("Enter a choice - ")
    if choice == '1':
        add_student()
    elif choice == '2':
        update_marks()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        view_student()
    else:
        print("wrong choice")
