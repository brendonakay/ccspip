import time, unittest

from chapter_1.exercise_1 import fib


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self._started_at = time.time()

    def test_fib(self):
        assert fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025

    def test_speed_on_big_number(self):
        return fib(100)

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))
