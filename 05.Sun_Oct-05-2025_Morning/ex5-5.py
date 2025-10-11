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

users = [
    User('Harry', 'Nguyen', 22),
    User('Nhu', 'Hoang', 10),
    User('Linh', 'Pham', 18)
]

users[0].increment_login_attempts()
users[0].increment_login_attempts()
users[1].increment_login_attempts()
users[1].increment_login_attempts()
users[1].increment_login_attempts()
users[2].increment_login_attempts()
users[2].increment_login_attempts()
users[2].increment_login_attempts()
users[2].increment_login_attempts()

def get_login_attempts(user):
    return user.loginAttempts

max_user = max(users, key=get_login_attempts)
print(max_user)