level_count = {"INFO" : 0, "ERROR" : 0, "WARNING" : 0}

with open("company.log", "r") as log_file:
    print(log_file)
    for message in log_file:   #1st - 2025-02-27 00:34:57,659 - INFO - File uploaded successfully 
        # print(message)
        for count in level_count:   # 1st - INFO 2nd - error 
            print(count)
            if count in message:    
                level_count[count] += 1    # 1st - INFO : 1, 2nd - ERROR : 1, 3rd - WARNING : 1, 4th - INFO : 2

    print(level_count)

    
# we have multiple log level whose value is set to 0 key as the log level and value as the count of the occcurences 
# creating a log file 
# add logs with different levels using echo 
# open the log file 
# we will start with reading the log file 
# start iteration on the log file to get/read every line in the file which is present in it.
# we have a nested for loop which is iterating over the diffrent log level present in the level_count 
# start the conditional statement where if level is in 1st iteration of 1st for loop then the level = 1 and if it repeats level = level + 1 
# we found the occurences of levels present in the log file 
# print it out.

# Pseudo code: 

# 	Table : LOG=0, DEBUG=0, INFO=0
# Lookup : (LOG, DEBUG, ERROR, INFO)
# X = Read the file in a variable. 	
# Loop over X per line (data is the variable)  ( #[2025-02-20 10:15:45]: User logged in


# Loglevel = Extract key (LOG/INFO/DEBUG/ERROR) from this variable data  (which holds the per line value) = null  
# Check if loglevel is not null {
# Level = Check if LOGLEVEL (null) is part of the LOOKUP collection. 
# 	Update the table above with the occurrence of this log level
#  }
# ) 
































# import logging
# # name = 'not working'
# # logging.error('%s raised an error',)

# logging.basicConfig(
#     filename="company.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
# logging.info("User logged in")
# logging.error("Database connection failed")
# logging.warning("Disk space low")
# logging.info("File uploaded successfully")
# #log_count = 0
# level_count = {"INFO" : 0, "ERROR" : 0, "WARNING" : 0}

# with open("company.log", "r") as log_file:
#     for message in log_file:   #1st - 2025-02-27 00:34:57,659 - INFO - File uploaded successfully
#         # print(message)
#         for count in level_count:   # 1st - INFO 2nd - Error 3rd - warning
#             # print(count)
#             if count in message:    
#                 level_count[count] += 1    # 1st - INFO : 1, 2nd - ERROR : 1, 3rd - WARNING : 1, 4th - INFO : 2

#     print(level_count)
        
    
