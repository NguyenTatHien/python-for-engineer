class User:
    def __init__(self, firstName, lastName, age, login_attempts = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.loginAttempts = login_attempts

    def describe_user(self):
        print(f"Your information:\n{self.firstName}\n{self.lastName}\n{self.age}")

    def greet_user(self):
        print(f"Welcome {self.firstName} {self.lastName}")

    def increment_login_attempts(self):
        self.loginAttempts += 1
        print('loginAttempts: ', self.loginAttempts)
    
    def reset_login_attempts(self):
        self.loginAttempts = 0
        print('loginAttempts after reset: ', self.loginAttempts)

    def __str__(self):
        return f"{self.firstName} {self.lastName} (age: {self.age}, loginAttempts: {self.loginAttempts})"

class Admin(User):
    def __init__(self, firstName, lastName, age):
        super().__init__(firstName, lastName, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("\nAdmin privileges:")
        for p in self.privileges:
            print("-", p)

admin1 = Admin("Alice", "Smith", 30)
admin1.describe_user()
admin1.show_privileges()