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


class TestDog(TestAnimals, unittest.TestCase):
    validation = {'init': 100, 'run': 90, 'swim': 70, 'fly': 100}

    def setUp(self):
        self.animal = Dog("Bobik")


class TestCat(TestAnimals, unittest.TestCase):
    validation = {'init': 100, 'run': 95, 'swim': 100, 'fly': 100}

    def setUp(self):
        self.animal = Cat("Kitty")


class TestTiger(TestAnimals, unittest.TestCase):
    validation = {'init': 200, 'run': 180, 'swim': 160, 'fly': 200}

    def setUp(self):
        self.animal = Tiger("Kitty")


class TestFishSimple(TestAnimals, unittest.TestCase):
    validation = {'init': 100, 'run': 100, 'swim': 95, 'fly': 100}

    def setUp(self):
        self.animal = FishSimple("Snappy")


class TestFishCanFly(TestAnimals, unittest.TestCase):
    validation = {'init': 100, 'run': 100, 'swim': 95, 'fly': 80}

    def setUp(self):
        self.animal = FishCanFly("MightySnappy")


class TestDuck(TestAnimals, unittest.TestCase):
    validation = {'init': 100, 'run': 100, 'swim': 90, 'fly': 70}

    def setUp(self):
        self.animal = Duck("Govard")


if __name__ == '__main__':
    unittest.main()
