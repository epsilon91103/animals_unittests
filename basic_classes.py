class Animal:
    def __init__(self, name, energy, init_parameters=None):
        if init_parameters is None:
            init_parameters = {}

        if init_parameters:
            self.name = init_parameters['name']
            if 'energy' in init_parameters.keys():
                condition = init_parameters["energy"]
            else:
                condition = energy
        else:
            self.name = name
            condition = energy

        self.energy = condition

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
