from datetime import date

class Blobfish:
    """_summary_"""

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        """_summary_"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        """_summary_"""
        return f"{self.name} is a {self.species}"

class Goldfish:
    """_summary_"""

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        """_summary_"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        """_summary_"""
        return f"{self.name} is a {self.species}"

class Angelfish:
    """_summary_"""

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        """_summary_"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        """_summary_"""
        return f"{self.name} is a {self.species}"

class Eel:
    """_summary_"""

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        """_summary_"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        """_summary_"""
        return f"{self.name} is a {self.species}"


class Pufferfish:
    """_summary_"""

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        """_summary_"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        """_summary_"""
        return f"{self.name} is a {self.species}"
