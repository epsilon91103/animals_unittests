from basic_classes import RunAnimal, SwimAnimal


class Dog(RunAnimal, SwimAnimal):
    def __init__(self, name, energy=100, **init_parameters):
        super().__init__(name, energy, **init_parameters)
