import re
import time
import json
import msvcrt
import yaml
import tkinter
from tkinter import ttk
import azure.cognitiveservices.speech as speechsdk
from azure.storage.blob import ContainerClient
from speech_recognition import recognize_from_microphone
from server import *
#git add --all
#git commit -m "hackhive"
#git push origin main 

darkMode_dark = "#282A36"
darkMode_navy = "#2C2F3D"
darkMode_grey = "#252526"
white = "#FFFFFF"

class Patient:
    def __init__(self, firstName, lastName, birthday, married, checkIn, phone, address, email, doctor, occupation, allergies, conditions,gender, sex, ethnicity, image, insurance, credit_card, height, weight, emergency_contact, emergency_contact_number):
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
        self.married = married
        self.checkIn = checkIn
        self.phone = phone
        self.address = address
        self.email = email
        self.doctor = doctor
        self.occupation = occupation
        self.allergies = allergies
        self.conditions = conditions
        self.gender = gender
        self.sex = sex
        self.gender = gender
        self.ethnicity = ethnicity
        self.image = image
        self.insurance = insurance
        self.credit_card = credit_card
        self.height = height
        self.weight = weight
        self.emergency_contact = emergency_contact
        self.emergency_contact_number = emergency_contact_number
    
        self.patient_dict = {
            "First Name": self.firstName,
            "Last Name": self.lastName,
            "Birthday": self.birthday,
            "Married": self.married,
            "Check In Time": self.checkIn,
            "Phone": self.phone,
            "Address": self.address,
            "Email": self.email,
            "Doctor": self.doctor,
            "Occupation": self.occupation,
            "Allergies": self.allergies,
            "Conditions": self.conditions,
            "Gender": self.gender,
            "Sex": self.sex,
            "Gender": self.gender,
            "Ethnicity":self.ethnicity,
            "Image": self.image,
            "Insurance": self.insurance,
            "Credit Card": self.credit_card,
            "Height": self.height,
            "Weight": self.weight,
            "Emergency Contact": self.emergency_contact,
            "Emergency Contact Number": self.emergency_contact_number
            
            }
        
        with open('patient_data.json', 'a') as a:
            json.dump(self.patient_dict, a)
            a.write('\n')

        #WE LOVE DEBUGGING
        #for key, value in self.patient_dict.items():
        #    print(f"{key}: {value}")

    
    #check if users phone number configuration is valid
def validate_phone(phone):
    #'905-721-8668' OR '9057218668'
    while not re.match("^(?!.*\(\d{3}\)\d{3}-\d{4}$)\(?\d{3}\)?-?\d{3}-?\d{4}$", phone):
        #print("Invalid phone number format. Please try again.")
        phone = input("Enter Phone Number: ")
    return phone

class Staff:
    def __init__(self, firstName, lastName, job_title, birthday) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.job_title = job_title
        self.birthday = birthday
        self.staff_dict = {}

    def get_info(self):
        self.staff_dict = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "job": self.job_title,
            "birthday": self.birthday
        }
        return self.staff_dict
#check if user email is valid
def validate_email(email):
    while not re.match("[^@]+@[^@]+\.[^@]+", email):
        #print("Invalid email format. Please try again.")
        email = input("Enter Email: ")
    return email
        
def current_time():
    localTime = time.localtime()
    current_time = time.strftime("%H:%M:%S", localTime)
    return current_time

def create_patient_from_input():
    firstName = left_entries["First Name"].get()
    lastName = left_entries["Last Name"].get()
    birthday = left_entries["Birthday"].get()
    married = left_entries["Married"].get()
    phone = left_entries["Phone"].get()
    address = left_entries["Address"].get()
    email = left_entries["Email"].get()
    doctor = left_entries["Doctor"].get()
    occupation = left_entries["Occupation"].get()
    allergies = left_entries["Allergies"].get()
    conditions = right_entries["Conditions"].get()
    gender = right_entries["Gender"].get()
    sex = right_entries["Sex"].get()
    ethnicity = right_entries["Ethnicity"].get()
    insurance = right_entries["Insurance"].get()
    credit_card = right_entries["Credit Card"].get()
    height = right_entries["Height"].get()
    weight = right_entries["Weight"].get()
    emergency_contact = right_entries["Emergency Contact"].get()
    emergency_contact_number = right_entries["EC Number"].get()

    create_patient = Patient(firstName, lastName, birthday, married, current_time(), phone, address, email, doctor, occupation, allergies, conditions, gender, sex, ethnicity, "Image", insurance, credit_card, height, weight, emergency_contact, emergency_contact_number)
    patient_creation_status.set("Data created!")
    return create_patient

def login():
    pass
# window setup
window = tkinter.Tk()
window.title("SmartHealth Records")
window.geometry("1920x1080")
window.iconbitmap("images\logo.ico")
window.configure(background=darkMode_dark)

style = ttk.Style()
style.configure("TFrame", background=darkMode_dark)  # Set background color for frames
style.configure("WhiteLabelBig.TLabel", foreground="white", background=darkMode_dark, font="Calibri 48 bold")
style.configure("WhiteLabelMed.TLabel", foreground="white", background=darkMode_dark, font="Calibri 24 bold")
style.configure("WhiteLabelSml.TLabel", foreground="white", background=darkMode_dark, font="Calibri 12 bold")
style.configure("WhiteLabelBut.TLabel", foreground="white", background=darkMode_grey, font="Calibri 32 bold")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(window)
notebook.pack(fill=tkinter.BOTH, expand=True)

#@----------------------------------------------------- Staff Register page -----------------------------------------------------
# Register page
frame_register = ttk.Frame(notebook, style="TFrame")
notebook.add(frame_register, text="Register Page")

welcome_text = ttk.Label(master=frame_register, text="Please enter the username of the new staff member: ", style="WhiteLabelBig.TLabel")
welcome_text.pack()

# Define label texts
label_texts = ["Username:", "Password:", "Confirm Password:", "First Name:", "Last Name:", "Birthday:", "Job Title:"]

# Create labels and entries
entry_widgets = {}  # Dictionary to store entry widgets

for label_text in label_texts:
    entry_frame = ttk.Frame(frame_register)
    entry_frame.pack(side='top', pady=5)

    label = ttk.Label(entry_frame, text=label_text, style="WhiteLabelBig.TLabel")
    label.grid(row=0, column=0, sticky='e')

    if label_text == "Password:":
        entry = ttk.Entry(entry_frame, font="Calibri 24 bold")
        new_password_entry = entry  # Assigning the variable to the entry
    elif label_text == "Confirm Password:":
        entry = ttk.Entry(entry_frame, font="Calibri 24 bold")
        confirm_password_entry = entry  # Assigning the variable to the entry
    elif label_text == "Job Title:":
        entry = ttk.Combobox(entry_frame, values=["1", "2", "3"], font="Calibri 24 bold")
    else:
        entry = ttk.Entry(entry_frame, font="Calibri 24 bold")

    entry.grid(row=0, column=1)

    # Save entry widget in the dictionary
    entry_widgets[label_text] = entry

# Store entry widgets in a list for easy access
entry_list = [entry_widgets[label_text] for label_text in label_texts]

# Label for displaying registration status
registration_status = tkinter.StringVar()
registration_status_label = ttk.Label(frame_register, textvariable=registration_status, style="WhiteLabelMed.TLabel")
registration_status_label.pack(pady=10)

def create_account():
    # Retrieve values from entry widgets
    username = entry_widgets["Username:"].get()
    new_password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Check if passwords match
    if new_password == confirm_password:
        #print("Successfully created account")
        try:
            # Load existing data from the user database file
            with open('user_database.json', 'r') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is empty, initialize an empty dictionary
            user_data = {}

        # Check if username already exists
        if username in user_data:
            registration_status.set("Username already exists. Choose a different username.")
            return

        # Add the new user's data to the dictionary
        user_data[username] = new_password

        # Save the updated data to the user database file
        with open('user_database.json', 'w') as file:
            json.dump(user_data, file)

        # Retrieve values for staff_data.json
        first_name = entry_widgets["First Name:"].get()
        last_name = entry_widgets["Last Name:"].get()
        birthday = entry_widgets["Birthday:"].get()
        job_title = entry_widgets["Job Title:"].get()

        # Create a dictionary for staff data
        staff_data = {
            "first_name": first_name,
            "last_name": last_name,
            "birthday": birthday,
            "job_title": job_title
        }

        # Append staff data to staff_data.json
        with open('staff_data.json', 'a') as file:
            json.dump(staff_data, file)
            file.write('\n')

        registration_status.set("Successfully created account")
    else:
        registration_status.set("Passwords do not match. Please try again.")

# Create Account button
create_account_button = ttk.Button(frame_register, text="Create Account", command=create_account, style="WhiteLabelBut.TLabel")
create_account_button.pack()
#@----------------------------------------------------- Staff Login page -----------------------------------------------------
# Login page
frame_login = ttk.Frame(notebook, style="TFrame")
notebook.add(frame_login, text="Login Page")

welcome_text = ttk.Label(master=frame_login, text="User Login", style="WhiteLabelBig.TLabel")
welcome_text.pack()

def load_user_database():
    try:
        with open('user_database.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_database(user_database):
    with open('user_database.json', 'w') as file:
        json.dump(user_database, file)

def getpass_with_mask(prompt=""):
    password = ""
    print(prompt, end='', flush=True)
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r':
            print()  # Move to the next line after password entry
            break
        elif char == '\x08':  # Backspace
            if password:
                password = password[:-1]
                print('\x08 \x08', end='', flush=True)  # Move back, overwrite '*', move back
        else:
            password += char
            print('*', end='', flush=True)  # Print '*' for masking
    return password

def login():
    # Get values from username and password entries
    username_input_value = username_input.get()
    password_input_value = password_input.get()

    # Load user database
    user_database = load_user_database()

    # Perform login check
    if username_input_value in user_database:
        stored_password = user_database[username_input_value]
        if stored_password == password_input_value:
            login_status.set("Login successful.")
            for key in user_database.keys():
                if key == username_input_value:
                    login_status.set(f"Welcome {key}!")
        else:
            login_status.set("Incorrect password. Please try again.")
    else:
        login_status.set("Username not found. Please register.")

# Frame for username
username_frame = ttk.Frame(frame_login)
username_frame.pack(pady=10)

# Label for username
username_label = ttk.Label(username_frame, text="Username:", style="WhiteLabelBig.TLabel")
username_label.pack(side=tkinter.LEFT, padx=(0, 10))

# Entry widget for username
username_input = ttk.Entry(username_frame, font="Calibri 24 bold")
username_input.pack(side=tkinter.LEFT)

# Frame for password
password_frame = ttk.Frame(frame_login)
password_frame.pack(pady=10)

# Label for password
password_label = ttk.Label(password_frame, text="Password:", style="WhiteLabelBig.TLabel")
password_label.pack(side=tkinter.LEFT, padx=(0, 10))

# Entry widget for password
password_input = ttk.Entry(password_frame, show="*", font="Calibri 24 bold")  # Use show="*" to mask the password
password_input.pack(side=tkinter.LEFT)

# Login button
login_button = ttk.Button(frame_login, text="Login", command=login, style="WhiteLabelBut.TLabel")
login_button.pack(pady=10)

# Label for displaying login status
login_status = tkinter.StringVar()
login_status_label = ttk.Label(frame_login, textvariable=login_status, style="WhiteLabelMed.TLabel")
login_status_label.pack(pady=10)

#@----------------------------------------------------- Patient page -----------------------------------------------------
# Patient page
frame_patient = ttk.Frame(notebook, style="TFrame")
notebook.add(frame_patient, text="Patient Page")

# Form layout on the left side of the page
left_frame = ttk.Frame(frame_patient, style="TFrame")
left_frame.grid(row=0, column=0, padx=20, pady=20)

# Form layout on the right side of the page
right_frame = ttk.Frame(frame_patient, style="TFrame")
right_frame.grid(row=0, column=1, padx=20, pady=20)

# Attribute labels and entry widgets on the left side
left_attributes = ["First Name", "Last Name", "Birthday", "Married", "Phone", "Address", "Email", "Doctor", "Occupation", "Allergies"]
left_entries = {}

for row, attribute in enumerate(left_attributes):
    label = ttk.Label(left_frame, text=f"{attribute}:", style="WhiteLabelBig.TLabel")
    label.grid(row=row, column=0, sticky=tkinter.W, padx=(0, 10))

    entry = ttk.Entry(left_frame, font="Calibri 24 bold")
    entry.grid(row=row, column=1)
    left_entries[attribute] = entry

# Attribute labels and entry widgets on the right side
right_attributes = ["Conditions", "Gender", "Sex", "Ethnicity", "Insurance", "Credit Card", "Height", "Weight", "Emergency Contact", "EC Number"]
right_entries = {}

for row, attribute in enumerate(right_attributes):
    label = ttk.Label(right_frame, text=f"{attribute}:", style="WhiteLabelBig.TLabel")
    label.grid(row=row, column=0, sticky=tkinter.W, padx=(0, 10))

    entry = ttk.Entry(right_frame, font="Calibri 24 bold")
    entry.grid(row=row, column=1)
    right_entries[attribute] = entry

# Submit button
submit_form_button = ttk.Button(frame_patient, text="Create Patient", command=create_patient_from_input, style="WhiteLabelBut.TLabel")
submit_form_button.grid(row=1, column=2, pady=10)

# Label for displaying patient creation status
patient_creation_status = tkinter.StringVar()
patient_creation_status_label = ttk.Label(frame_patient, textvariable=patient_creation_status, style="WhiteLabelMed.TLabel")
patient_creation_status_label.grid(row=2, column=2, pady=10)
#@----------------------------------------------------- Speech Page -----------------------------------------------------
# Speech page
frame_speech = ttk.Frame(notebook, style="TFrame")
notebook.add(frame_speech, text="Speech Page")

welcome_text = ttk.Label(master=frame_speech, text="Press to Record", style="WhiteLabelBig.TLabel")
welcome_text.pack()
login_button = ttk.Button(frame_speech, text="press", command=recognize_from_microphone, style="WhiteLabelBut.TLabel")
login_button.pack()

#@----------------------------------------------------- Server Page -----------------------------------------------------
# Server page #todo ADD IN THE STAFF AND STAFF LOGIN
frame_server = ttk.Frame(notebook, style="TFrame")
notebook.add(frame_server, text="Upload Page")

welcome_text = ttk.Label(master=frame_server, text="Press to Upload Data", style="WhiteLabelBig.TLabel")
welcome_text.pack()
login_button = ttk.Button(frame_server, text="upload", command=run_jitt, style="WhiteLabelBut.TLabel")
login_button.pack()

# Show the notebook
notebook.pack()

# loop
window.mainloop()
