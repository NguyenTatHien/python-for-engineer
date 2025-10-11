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
export.describe_restaurant()
export2 = Restaurant("Happy food 2", "Fast food 2")
export2.describe_restaurant()
export3 = Restaurant("Happy food 3", "Fast food 3")
export3.describe_restaurant()