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
        self.animal = Dog("Bobik", run_energy=10, swim_energy=30)


class TestCat(TestAnimals, unittest.TestCase):
    validation = {'init': 100, 'run': 95, 'swim': 100, 'fly': 100}

    def setUp(self):
        self.animal = Cat("Kitty", run_energy=5)


class TestTiger(TestAnimals, unittest.TestCase):
    validation = {'init': 200, 'run': 180, 'swim': 160, 'fly': 200}

    def setUp(self):
        self.animal = Tiger("Kitty", swim_energy=40, run_energy=20)


class TestFishSimple(TestAnimals, unittest.TestCase):
    validation = {'init': 100, 'run': 100, 'swim': 95, 'fly': 100}

    def setUp(self):
        self.animal = FishSimple("Snappy", swim_energy=5)


class TestFishCanFly(TestAnimals, unittest.TestCase):
    validation = {'init': 100, 'run': 100, 'swim': 95, 'fly': 80}

    def setUp(self):
        self.animal = FishCanFly("MightySnappy", swim_energy=5, fly_energy=20)


class TestDuck(TestAnimals, unittest.TestCase):
    validation = {'init': 100, 'run': 100, 'swim': 90, 'fly': 70}

    def setUp(self, a=5):
        self.animal = Duck("Govard", swim_energy=10, fly_energy=30)


if __name__ == '__main__':
    unittest.main()
