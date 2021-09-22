import unittest
import sunny

class TestSunny(unittest.TestCase):

    #function to test if it won't be sunny
    def test_sunny(self):
        self.assertEqual(sunny.chancesOfSun(14), None)

    #function to test if it will be sunny
    def test_sunny2(self):
        self.assertEqual(sunny.chancesOfSun(21), None)

    #function to test if it may be sunny
    def test_sunny3(self):
        self.assertEqual(sunny.chancesOfSun(17), None)

if __name__ == '__main__':
    unittest.main()