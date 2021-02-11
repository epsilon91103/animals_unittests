from basic_classes import RunAnimal, SwimAnimal


class Cat(RunAnimal):
    def __init__(self, name, energy=100, **init_parameters):
        super().__init__(name, energy, **init_parameters)


class Tiger(Cat, SwimAnimal):
    def __init__(self, name, energy=200, **init_parameters):
        super().__init__(name, energy, **init_parameters)
