import random, time, unittest

from typing import List

from chapter_2.exercise_1 import binary_contains, linear_contains

TestList = List[int] # type aloas for test list of one million numbers


def generate_random_testlist() -> TestList:
    tl: TestList = [ random.choice(range(1, 100000)) for _ in range(1,1000000) ]
    return tl


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self._started_at: time = time.time()
        print("Creating Test List")
        self._tl: TestList = generate_random_testlist()

    def test_linear_contains(self):
        """
        Test chapter_2.exercise_1.linear_contains
        This test runs the function 5 times using a randomly generated key to
        find in a randomly generated list of one million integers that range
        from 1 to 100
        """
        for i in range(1,5):
            key = random.choice(range(1, 100000))
            print(f"Using linear search to find random key: {key}")
            results, hop_count = linear_contains(self._tl, key)
            if results:
                print(f"Found key {key} in {hop_count} hops")
            else:
                print(f"Key {key} was not found in {hop_count} hops")

    def test_binary_contains(self):
        for i in range(1,5):
            key = random.choice(range(1, 100000))
            print(f"Using binary search to find random key: {key}")
            results, hop_count = binary_contains(self._tl, key)
            if results:
                print(f"Found key {key} in {hop_count} hops")
            else:
                print(f"Key {key} was not found in {hop_count} hops")

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))
