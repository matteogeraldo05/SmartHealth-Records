class Staff:
    def __init__(self, firstName, lastName, job_title, birthday, authority, SIN) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.job_title = job_title
        self.birthday = birthday
        self.authority = authority
        self.__SIN = SIN

        self.staff_dict = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "job": self.job_title,
            "birthday": self.birthday,
            "authority": self.authority,
        }


def create_staff():
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    birthday = input("Enter Birthday: ")
    job_title = input("Job Title: ")
    authority = input("Authority Level: ")
    SIN = input("SIN: ")
    return Staff(firstName, lastName, birthday, job_title, authority, SIN)
