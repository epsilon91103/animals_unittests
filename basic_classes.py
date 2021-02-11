class Animal:
    def __init__(self, name, energy, **init_parameters):
        self.name = init_parameters.get('name', name)
        self.energy = init_parameters.get('energy', energy)

    def say(self):
        print(f"Hello, i'm {type(self).__name__} and my name is {self.name}")

    def run(self):
        print(f"My name is '{self.name}' and i can't run")

    def swim(self):
        print(f"My name is '{self.name}' and i can't swim")

    def fly(self):
        print(f"My name is '{self.name}' and i can't fly")

    def get_energy(self):
        return self.energy


class RunAnimal(Animal):
    def __init__(self, name, energy, **init_parameters):
        super().__init__(name, energy, **init_parameters)
        self.run_energy = init_parameters['run_energy']

    def run(self):
        print(f"My name is '{self.name}' and i running")
        self.energy -= self.run_energy


class SwimAnimal(Animal):
    def __init__(self, name, energy, **init_parameters):
        super().__init__(name, energy, **init_parameters)
        self.swim_energy = init_parameters['swim_energy']

    def swim(self):
        print(f"My name is '{self.name}' and i swimming")
        self.energy -= self.swim_energy


class FlyAnimal(Animal):
    def __init__(self, name, energy, **init_parameters):
        super().__init__(name, energy, **init_parameters)
        self.fly_energy = init_parameters['fly_energy']

    def fly(self):
        print(f"My name is '{self.name}' and i flying")
        self.energy -= self.fly_energy
