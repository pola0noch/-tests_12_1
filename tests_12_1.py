import unittest
from unittest import TestCase

import runner

class RunnerTest(TestCase):
    def test_walk(self):
        test_w = runner.Runner("Test walk")
        for i in range(10):
            test_w.walk()
        self.assertEqual(test_w.distance, 50)

    def test_run(self):
        test_r = runner.Runner("Test run")
        for i in range(10):
            test_r.run()
        self.assertEqual(test_r.distance, 100)

    def test_challenge(self):
        test_1 = runner.Runner("runner1")
        test_2 = runner.Runner("runner2")
        for i in range(10):
            test_1.walk()
            test_2.run()
        self.assertNotEqual(test_1.distance, test_2.distance)

if __name__ == '__main__':
    unittest.main()





