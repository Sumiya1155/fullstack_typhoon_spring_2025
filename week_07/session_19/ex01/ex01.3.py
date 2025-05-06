class Cat:
    species = "Felis catus"
    def __init__(self, name, color, age ):
        self.name = name
        self.color = color
        self.age = age * 7
    def change_name(self, name):
        self.name = name
        return f"{self.name}"
mittens = Cat("Mittens", "white", 3)
luna = Cat("luna", "black" 2)

print(f"Species: {Cat.species}")