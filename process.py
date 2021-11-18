log_file = open("um-server-01.txt") # this allows us to access the files in the file


def sales_reports(log_file): #this is a fuction that has a for loop in it that accesses the file 
    for line in log_file: # creates value to look up in file 
        line = line.rstrip() #strips of any whitespace when we print the file information
        day = line[0:3] # this selects a certain line in the file
        if day == "Mon": #this looks to see if the day equals the string "Mon"
            print(line) #shows the information we looked up


sales_reports(log_file) #shows information from the function sales_reports
