class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def meow(self):
        return f"Meow I'm a {self.name}"
    def __str__(self):
        return f"{self.name} is a {self.color} cat"
    def __repr__(self):
        return f"cat(name={self.name}, color={self.color})"

mittens = Cat("Mittens", "white")
luna = Cat("luna", "black")
print(mittens)
print(repr(mittens))
print(repr(luna))
print(luna)

