class User:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    def describe_user(self):
        print(f"Your information:\n{self.firstName}\n{self.lastName}\n{self.age}")
    def greet_user(self):
        print(f"Welcome {self.firstName} {self.lastName}")

ex = User('Harry', 'Nguyen', 22)
ex.describe_user()
ex.greet_user()

ex = User('Hoang', 'Nhu', 20)
ex.describe_user()
ex.greet_user()