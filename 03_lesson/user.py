class User:

    firstName = 'Alex'
    lastName = 'G'

    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name

    def fName(self, name):
        print("Имя:", self.firstName)

    def lName(self, lname):
        print("Фамилия:", self.lastName)

    def flname(self, flname):
        print("Имя и фамилия:", self.firstName, self.lastName)
