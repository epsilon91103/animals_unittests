import unittest
from dogs import Dog
from cats import Cat, Tiger
from fish import FishSimple, FishCanFly
from ducks import Duck


class TestAnimals:
    def test_init(self):
        self.animal.say()
        self.assertEqual(self.animal.get_energy(), self.results['init'])

    def test_run(self):
        self.animal.run()
        self.assertEqual(self.animal.get_energy(), self.results['run'])

    def test_swim(self):
        self.animal.swim()
        self.assertEqual(self.animal.get_energy(), self.results['swim'])

    def test_fly(self):
        self.animal.fly()
        self.assertEqual(self.animal.get_energy(), self.results['fly'])


class TestDog(TestAnimals, unittest.TestCase):
    def setUp(self):
        self.animal = Dog("Bobik")
        self.results = {'init': 100, 'run': 90, 'swim': 70, 'fly': 100}


class TestCat(TestAnimals, unittest.TestCase):
    def setUp(self):
        self.animal = Cat("Kitty")
        self.results = {'init': 100, 'run': 95, 'swim': 100, 'fly': 100}


class TestTiger(TestAnimals, unittest.TestCase):
    def setUp(self):
        self.animal = Tiger("Kitty")
        self.results = {'init': 200, 'run': 180, 'swim': 160, 'fly': 200}


class TestFishSimple(TestAnimals, unittest.TestCase):
    def setUp(self):
        self.animal = FishSimple("Snappy")
        self.results = {'init': 100, 'run': 100, 'swim': 95, 'fly': 100}


class TestFishCanFly(TestAnimals, unittest.TestCase):
    def setUp(self):
        self.animal = FishCanFly("MightySnappy")
        self.results = {'init': 100, 'run': 100, 'swim': 95, 'fly': 80}


class TestDuck(TestAnimals, unittest.TestCase):
    def setUp(self):
        self.animal = Duck("Govard")
        self.results = {'init': 100, 'run': 100, 'swim': 90, 'fly': 70}


if __name__ == '__main__':
    unittest.main()
