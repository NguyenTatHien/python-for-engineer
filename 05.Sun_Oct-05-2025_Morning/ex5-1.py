class Restaurant():
    def __init__(self, rn, ct):
        self.restaurant_name = rn
        self.cuisine_type = ct
    
    def describe_restaurant(self):
        print('Restaurant name: ', self.restaurant_name)
        print('Cuisine type: ', self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open.")

export = Restaurant("Happy food", "Fast food")
print('First attribute: ', export.restaurant_name)
print('Second attribute: ', export.cuisine_type)
export.describe_restaurant()
export.open_restaurant()