class Restaurant():
    def __init__(self, rn, ct, number_served):
        self.restaurant_name = rn
        self.cuisine_type = ct
        self.number_served = number_served
        self.flavors = []

    def describe_restaurant(self):
        print('Restaurant name: ', self.restaurant_name)
        print('Cuisine type: ', self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, n):
        self.number_served = n
    
    def increment_number_served(self, n):
        self.number_served += n

class IceCreamStand(Restaurant):
    def __init__(self, rn, ct="Ice Cream", number_served=0):
        super().__init__(rn, ct, number_served)
        self.flavors = ["vanilla", "chocolate", "strawberry", "mint"]
    
    def display_flavors(self):
        print("\nAvailable ice cream flavors:")
        for flavor in self.flavors:
            print("-", flavor)

ice_cream_stand = IceCreamStand("Happy Ice")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()