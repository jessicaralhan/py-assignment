import csv
def generate_email(name):
    first, last = name.split()
    return(f"{first.lower()}.{last.lower()}@company.com")
with open("details.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    employees = list(reader)
for details in employees:
    name, department = details
    email = generate_email(name)
    details.append(email)

with open("newdata.csv", "w", newline='') as newfile:
    writer = csv.writer(newfile)
    writer.writerow(["Name, Department, Email"])
    writer.writerows(employees)

print("saved in newfile")



# import the required packages 
# open a file i.e details.csv and read from it csv.reader(file) 
# in first line we have header so we move reader to the next row
# employees has the list with name, department in it
# now we need to generate emails where we use split function on name and it splits the first and last name 
# we are returning emails 
# iterating over employees which currently and name and department in it. So value of details = name, department and email get the values from generate_email function
# details already had name, department then we will add email in it 
# open a newfile and write in it 
# add first new which in heading 
# and in other rows we will add the respective values 





















# with open("details.csv", "r") as csv_file:
# for data in csv_file:
#     print(data)
# with open("newdata.csv", "w") as new_file:
#     new_file.write("jessica")
    
    # writer = csv.writer(csv_file)
    # for word in csv_file:
    #     writer.writerow(column)
    # writer.writecolumn(word)
# for data in csv_file:
#     print(data)
#     writer = csv.writer(csv_file)
#     writer.writerow(column)
# print("done")


































# import pandas as pd 
# df = pd.DataFrame(
#     {
#         "Name" : [
#             "John Doe",
#             "Jane Smith",
#             "Alice Brown"
#         ],
#         "Department" : [
#             "Sales",
#             "Engineering",
#             "HR"
#         ],
#         "Email" : [
#             "john.doe@company.com",
#             "jane.smith@company.com",
#             "alice.brown@company.com"
#         ]
#     }
# )
# print(df)

