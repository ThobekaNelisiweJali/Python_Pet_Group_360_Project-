class Pet:
    def __init__(self, name):
        # Sup team! My name is Thembelani, I prefer being called Sipho.
        # This is our constructor method. It initializes our pet with default attributes.
        # The 'self' keyword refers to the instance of the class itself.
        self.name = name  # Each pet has a name, which is passed when the object is created.
        self.hunger = 5  # Hunger level starts at a neutral point (0 = full, 10 = very hungry).
        self.energy = 5  # Energy level also starts in the middle (0 = exhausted, 10 = fully rested).
        self.happiness = 5  # Happiness is initially neutral (scale of 0-10).
        self.tricks = []  # This list will store any tricks the pet learns.

    def eat(self):
        # This method simulates the pet eating.
        # Eating reduces hunger by 3, but doesn't let it drop below 0.
        # Also, eating makes the pet slightly happier.
        self.hunger = max(0, self.hunger - 3)  # Using 'max' ensures hunger never goes below 0.
        self.happiness = min(10, self.happiness + 1)  # Happiness increases but is capped at 10.

    def sleep(self):
        # This method allows the pet to sleep and regain energy.
        # It increases energy by 5, but doesn't let it exceed 10.
        self.energy = min(10, self.energy + 5)  # Using 'min' ensures energy never exceeds 10.

    def play(self):
        # Playing with the pet affects multiple attributes.
        # It decreases energy, increases happiness, and makes the pet slightly hungrier.
        self.energy = max(0, self.energy - 2)  # Playing reduces energy by 2, but it can’t go below 0.
        self.happiness = min(10, self.happiness + 2)  # Playing makes the pet happier.
        self.hunger = min(10, self.hunger + 1)  # Activity makes pets hungry, so hunger slightly increases.

    def get_status(self):
        # This method prints the pet's current state.
        # It provides a summary of hunger, energy, and happiness levels.
        print(f"{self.name}'s status - Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")

    def train(self, trick):
        # This method allows the pet to learn new tricks.
        # We simply append the new trick to the tricks list and display a message.
        self.tricks.append(trick)  # Adding the learned trick to the list.
        print(f"{self.name} learned a new trick: {trick}!")  # Confirming the trick was learned.

    def show_tricks(self):
        # This method displays all the tricks the pet has learned.
        if self.tricks:  # If the list isn’t empty, print all learned tricks.
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")  # Formatting the tricks list.
        else:
            print(f"{self.name} hasn't learned any tricks yet.")  # If no tricks were learned, print a message.

# Here’s an example how we create a pet and interact with its abilities.

my_pet = Pet("Blackie")  # Creating a pet named Blackie after my own dog.
my_pet.eat()  # Feeding Blackie.
my_pet.play()  # Playing with Blackie.
my_pet.train("Roll over")  # Teaching Blackie a trick.
my_pet.show_tricks()  # Showing all learned tricks.
my_pet.get_status()  # Displaying Blackie's current status.