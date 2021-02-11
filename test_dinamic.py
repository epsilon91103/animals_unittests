import unittest
from dogs import Dog
from cats import Cat, Tiger
from fish import FishSimple, FishCanFly
from ducks import Duck


class TestInitAnimals:
    def test_init(self):
        self.animal.say()
        self.assertEqual(self.animal.get_energy(), self.validation['init'])


class TestRunAnimals:
    def test_run(self):
        self.animal.run()
        self.assertEqual(self.animal.get_energy(), self.validation['run'])


class TestSwimAnimals:
    def test_swim(self):
        self.animal.swim()
        self.assertEqual(self.animal.get_energy(), self.validation['swim'])


class TestFlyAnimals:
    def test_fly(self):
        self.animal.fly()
        self.assertEqual(self.animal.get_energy(), self.validation['fly'])


def create_method(animal, args):
    def setUp(self):
        self.animal = animal(**args)
    return setUp


if __name__ == '__main__':
    base_classes = {'init': TestInitAnimals, 'run': TestRunAnimals, 'swim': TestSwimAnimals, 'fly': TestFlyAnimals}
    tests = (
        [
            Dog,
            {'name': 'Bobik', 'run_energy': 10, 'swim_energy': 30},
            {'init': 100, 'run': 90, 'swim': 70, 'fly': 100}],
        [
            Cat,
            {'name': 'Kitty', 'run_energy': 5},
            {'init': 100, 'run': 95, 'swim': 100, 'fly': 100}],
        [
            Tiger,
            {'name': 'BigKitty', 'run_energy': 20, 'swim_energy': 40},
            {'init': 200, 'run': 180, 'swim': 160, 'fly': 200}],
        [
            FishSimple,
            {'name': 'FishSimple', 'swim_energy': 5},
            {'init': 100, 'run': 100, 'swim': 95, 'fly': 100}],
        [
            FishCanFly,
            {'name': 'MightySnappy', 'swim_energy': 5, 'fly_energy': 20},
            {'init': 100, 'run': 100, 'swim': 95, 'fly': 80}],
        [
            Duck,
            {'name': 'Govard', 'swim_energy': 10, 'fly_energy': 30},
            {'init': 100, 'run': 100, 'swim': 90, 'fly': 70}],
        [
            FishCanFly,
            {'name': 'MightySnappy', 'swim_energy': 5, 'fly_energy': 20},
            {'init': 100, 'run': 100, 'swim': 95, 'fly': 80}],
    )
    for (class_, params_init, validation) in tests:
        name = f'Test{class_.__name__}'
        bases = tuple(base_classes[test_name] for test_name in validation) + (unittest.TestCase,)
        new_class = type(name, bases, {})
        new_class.validation = validation
        new_class.setUp = create_method(class_, params_init)
        globals()[name] = new_class
    del new_class

    unittest.main()
