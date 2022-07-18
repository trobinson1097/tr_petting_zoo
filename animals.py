from models import (Giraffe, Zebra, Donkey, Goat, Llama,
    Salamander, Ratsnake, Copperhead, Lizard, Hellbender,
    Blobfish, Goldfish, Angelfish, Pufferfish, Eel)


elmo = Eel("Elmo", "electric eel")

poko = Pufferfish("Poko", "pufferfish")

angie = Angelfish("Angie", "freshwater angelfish")

goldie= Goldfish("Goldie", "bubbleye goldfish")

boo = Blobfish("Boo", "Blobfish")

hammy = Hellbender("Hammy", "wild hellbender")

randy = Ratsnake("Randy", "wild rat snake")

coco = Lizard("Coco", "wild australian gecko")

sally = Salamander("Sally", "domestic salamander")

mango = Copperhead("Mango", "wild copperhead")

moe = Donkey("Moe", "domestic donkey", "midday")

eddy = Goat("Eddy", "domestic goat", "afternoon")

zoey = Zebra("Zoey", "Domestic zebra", "morning")

goody = Giraffe("Goody", "domestic giraffe", "midday")

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning")

print(f'{goody.name} the {goody.species} is availabe to pet during {goody.shift} shift.')
