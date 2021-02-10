import unittest
from dogs import Dog
from cats import Cat, Tiger
from fish import FishSimple, FishCanFly
from ducks import Duck


class TestAnimals:
    validation = {}

    def test_init(self):
        self.animal.say()
        self.assertEqual(self.animal.get_energy(), self.validation['init'])

    def test_run(self):
        self.animal.run()
        self.assertEqual(self.animal.get_energy(), self.validation['run'])

    def test_swim(self):
        self.animal.swim()
        self.assertEqual(self.animal.get_energy(), self.validation['swim'])

    def test_fly(self):
        self.animal.fly()
        self.assertEqual(self.animal.get_energy(), self.validation['fly'])


def create_method(animal, args):
    def setUp(self):
        self.animal = animal(*args)
    return setUp


if __name__ == '__main__':
    tests = (
        [Dog, ('Bobik',), {'init': 100, 'run': 90, 'swim': 70, 'fly': 100}],
        [Cat, ('Kitty',), {'init': 100, 'run': 95, 'swim': 100, 'fly': 100}],
        [Tiger, ('BigKitty',), {'init': 200, 'run': 180, 'swim': 160, 'fly': 200}],
        [FishSimple, ('FishSimple',), {'init': 100, 'run': 100, 'swim': 95, 'fly': 100}],
        [FishCanFly, ('MightySnappy',), {'init': 100, 'run': 100, 'swim': 95, 'fly': 80}],
        [Duck, ('Govard',), {'init': 100, 'run': 100, 'swim': 90, 'fly': 70}],
    )
    for (class_, params_init, validation) in tests:
        name = f'Test{class_.__name__}'
        new_class = type(name, (TestAnimals, unittest.TestCase), {})
        new_class.validation = validation
        new_class.setUp = create_method(class_, params_init)
        globals()[name] = new_class
    del new_class

    unittest.main()
