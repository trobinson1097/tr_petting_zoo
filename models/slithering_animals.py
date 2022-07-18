from datetime import date

class Copperhead:
    """_summary_"""

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        """_summary_"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Salamander:
    """_summary_"""

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        """_summary_"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Lizard:
    """_summary_"""

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        """_summary_"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Ratsnake:
    """_summary_"""

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        """_summary_"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Hellbender:
    """_summary_"""

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        """_summary_"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"
