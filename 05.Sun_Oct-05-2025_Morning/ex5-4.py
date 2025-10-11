class Restaurant():
    def __init__(self, rn, ct, number_served):
        self.restaurant_name = rn
        self.cuisine_type = ct
        self.number_served = number_served

    def describe_restaurant(self):
        print('Restaurant name: ', self.restaurant_name)
        print('Cuisine type: ', self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, n):
        self.number_served = n
    
    def increment_number_served(self, n):
        self.number_served += n

export = Restaurant("Happy food", "Fast food", 0)
export.set_number_served(10)
print(f'First served: {export.number_served}')
export.increment_number_served(20)
print(f'Second served after increment: {export.number_served}')
