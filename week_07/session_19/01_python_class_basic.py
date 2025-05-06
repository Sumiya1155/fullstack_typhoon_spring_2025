class Dog:

    """Engiin nohoi klass"""



    pass

banhar = Dog() # object - bodit zuil
print(banhar)
bulldog = Dog()
print(bulldog)

# __int__ gedeg klass punkts

class Cat:
    def __init__(self, name, race):
        self.name = name #class attributes, class varibles
        self.race = race

    def meow(self):
        return f"Meow! I'm a {self.name}"    
    def __str__(self):
        return f"{self.name} нь {self.race}"
    def __repr__(self):
        return f"Cat(name={self.name}, race={self.race})"
    

# cat gedeg class 2 turliin object buyu 2 turliin muur uusgene uu
# object oriented programming buyu obiekt handaltad programmchlal
koshka = Cat("Koshka", "Marine Coon")
print(koshka)
print(koshka.name)
print(koshka.meow())
print(repr(koshka))

# class identities
class Horse:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


black_horse = Horse("Har mori", 3)
print(black_horse.species)
print(black_horse.age)
print(black_horse.name)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old"
    def bark(self, sound):
        return f"{self.name} says {sound}"
    

baawgai = Dog(name="baawgai", age=5 )

print(baawgai.description())
print(baawgai.bark("Hov Hov"))
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance




class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("Fiddo")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")
print(d.tricks)
print(e.tricks)        
