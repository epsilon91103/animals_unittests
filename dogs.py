from basic_classes import Animal


class Dog(Animal):
    def __init__(self, name, energy=100, init_parameters=None):
        super().__init__(name, energy, init_parameters)

    def run(self):
        print(f"My name is '{self.name}' and i running")
        self.energy = self.energy - 10

    def swim(self):
        print(f"My name is '{self.name}' and i swimming")
        self.energy = self.energy - 30
