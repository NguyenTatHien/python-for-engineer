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
    
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges list:")
        for p in self.privileges:
            print("-", p)

class AdminWithPrivileges(User):
    def __init__(self, firstName, lastName, age):
        super().__init__(firstName, lastName, age)
        self.privileges = Privileges()


admin2 = AdminWithPrivileges("Bob", "Nguyen", "bob@example.com")
admin2.describe_user()
admin2.privileges.show_privileges()