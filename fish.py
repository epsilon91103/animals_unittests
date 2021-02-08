from basic_classes import Animal


class FishSimple(Animal):
    def __init__(self, name, energy=100, init_parameters=None):
        super().__init__(name, energy, init_parameters)

    def swim(self):
        print(f"My name is '{self.name}' and i swimming")
        self.energy = self.energy - 5


class FishCanFly(FishSimple):
    def __init__(self, name, energy=100, init_parameters=None):
        super().__init__(name, energy, init_parameters)

    def fly(self):
        print(f"My name is '{self.name}' and i flying")
        self.energy = self.energy - 20
