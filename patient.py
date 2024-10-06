import re
import time
import json

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
        
        with open('data.json', 'a') as a:
            json.dump(self.patient_dict, a)
            a.write('\n')

        for key, value in self.patient_dict.items():
            print(f"{key}: {value}")

    
    #check if users phone number configuration is valid
def validate_phone(phone):
    #'905-721-8668' OR '9057218668'
    while not re.match("^(?!.*\(\d{3}\)\d{3}-\d{4}$)\(?\d{3}\)?-?\d{3}-?\d{4}$", phone):
        print("Invalid phone number format. Please try again.")
        phone = input("Enter Phone Number: ")
    return phone

#check if user email is valid
def validate_email(email):
    while not re.match("[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format. Please try again.")
        email = input("Enter Email: ")
    return email
        
def current_time():
    localTime = time.localtime()
    current_time = time.strftime("%H:%M:%S", localTime)
    return current_time

def create_patient():
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    birthday = input("Enter Birthday: ")
    married = input("Married? YES or NO: ")
    checkIn = current_time()
    phone = input("Enter Phone Number: ")
    phone = validate_phone(phone)
    address = input("Enter Address: ")
    email = input("Enter Email: ")
    email = validate_email(email)
    doctor = input("Enter Doctor: ")
    occupation = input("Enter Occupation: ")  
    allergies = input("Enter Allergies: ").split()
    conditions = input("Enter Conditions: ").split()
    gender = input("Enter Gender:")
    sex = input("Enter Sex:")
    ethnicity = input("Enter Ethnicity: ")
    insurance = input("Enter Insurance: ")
    credit_card = int(input("Enter Credit Card: "))
    height = int(input("Enter Height (in): "))
    weight = int(input("Enter Weight (lbs): "))
    emergency_contact = input("Enter Emergency Contact: ")
    emergency_contact_number = input("Enter Emergency Number: ")

    return Patient(firstName, lastName, birthday, married, checkIn, phone, address, email, doctor, occupation, allergies, conditions,gender, sex,ethnicity,"Image",insurance,credit_card,height,weight,emergency_contact, emergency_contact_number)