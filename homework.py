class Dog:
    # Class variable shared among all instances
    species = "Canis lupus familiaris"
    
    def __init__(self, name, breed):
        # Instance variables unique to each instance
        self.name = name
        self.breed = breed
    
    def display_details(self):
        print(f"Dog Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 30)

# Creating instances of Dog with different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Displaying details of each dog
dog1.display_details()
dog2.display_details()
