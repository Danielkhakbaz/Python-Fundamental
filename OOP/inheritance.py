class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"I'm {self.name} and I'm {self.age} years old."

    def speak(self):
        return "I don't know what to say!"


class Dog(Pet):
    def speak(self):
        return "Bark!"


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        return f"I'm {self.name} and I'm {self.age} years old and I'm {self.color}."

    def speak(self):
        return "Meow"


unknown = Pet("Jim", 23)
print(unknown.speak())

dog = Dog("Doggy", 12)
print(dog.speak())

cat = Cat("Catty", 10, "Brown")
print(cat.show())
