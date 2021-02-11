from basic_classes import FlyAnimal, SwimAnimal


class FishSimple(SwimAnimal):
    def __init__(self, name, energy=100, **init_parameters):
        super().__init__(name, energy, **init_parameters)


class FishCanFly(FishSimple, FlyAnimal):
    def __init__(self, name, energy=100, **init_parameters):
        super().__init__(name, energy, **init_parameters)
