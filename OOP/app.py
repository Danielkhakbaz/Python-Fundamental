class Dog:
    def __init__(self, name):
        self.name = name

    def add_one(self, number):
        print(number + 1)
        print(self.name)

    def minus_one(self, number):
        return number - 1


a = Dog("Dani")
b = Dog("Bezi")

a.add_one(1)