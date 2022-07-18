from models import (Giraffe, Zebra, Donkey, Goat, Llama,
    Salamander, Ratsnake, Copperhead, Lizard, Hellbender,
    Blobfish, Goldfish, Angelfish, Pufferfish, Eel)


elmo = Eel("Elmo", "electric eel", "spagettie")

poko = Pufferfish("Poko", "pufferfish", "ramen")

angie = Angelfish("Angie", "freshwater angelfish", "tofu")

goldie= Goldfish("Goldie", "bubbleye goldfish", "fruity pebbles")

boo = Blobfish("Boo", "Blobfish", "air")

hammy = Hellbender("Hammy", "wild hellbender", "hammhocks")

randy = Ratsnake("Randy", "wild rat snake", "boiled eggs")

coco = Lizard("Coco", "wild australian gecko", "chrickets")

sally = Salamander("Sally", "domestic salamander", "fried rice")

mango = Copperhead("Mango", "wild copperhead", "fish eggs")

moe = Donkey("Moe", "domestic donkey", "midday", "corn")

eddy = Goat("Eddy", "domestic goat", "afternoon", "granola")

zoey = Zebra("Zoey", "Domestic zebra", "morning", "pizza")

goody = Giraffe("Goody", "domestic giraffe", "midday", "salad")

tina = Llama("Tina", "domestic llama", "morning", "slop")

#print(f'{goody.name} the {goody.species} is availabe to pet during {goody.shift} shift.')


print(tina.feed())
print(tina)
