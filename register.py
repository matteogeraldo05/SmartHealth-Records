import json
from staff import Staff

newUsername = input("Please enter the username of the new staff member: ")

while True:
    newPassword = input("Please enter a new password: ")
    test_Password = input("Re-enter the new password: ")

    if newPassword == test_Password:
        print("Successfully created account")
        try:
            with open('user_database.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        break
    else:
        print("You entered two different passwords, try again")

# Add the new staff member's information to the JSON data
data[newUsername] = newPassword

with open('user_database.json', 'w') as file:
    json.dump(data, file)

firstName = input("Enter First Name: ")
lastName = input("Enter Last Name: ")
birthday = input("Enter Birthday (yyyy/mm/dd or yyyymmdd): ")

job_title_mappings = {1: "Security Guard", 2: "Nurse", 3: "Doctor"}

while True:
    job_title_input = int(input("Enter Job Title (1 = Security Guard, 2 = Nurse, 3 = Doctor): "))

    if job_title_input >= 1 and job_title_input <= 3:
        job_title = int(job_title_input)
        if job_title in job_title_mappings:
            break
        else:
            print("Invalid job title. Please enter a valid job title.")
    else:
        print("Invalid input. Please enter a number.")

# Create a Staff object
staff_member = Staff(firstName, lastName, job_title_mappings[job_title], birthday)
staff_Data = staff_member.get_info()

print("Staff member information added to the database.")

with open('staff_Data.json', 'a') as file:
    json.dump(staff_Data, file)
    file.write('\n')