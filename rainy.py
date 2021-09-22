import unittest

# bringUmbrella function determines if an umbrella should be used based on the percentage of the chance of rain.
def bringUmbrella(chanceOfRain):
    if chanceOfRain >= 45:
        return True
    else:
        return False

# Calss for unit testing the bringUmbrella function. Tests both for chanceOfRain = 50 and chanceOfRain = 40.
class TestRain(unittest.TestCase):
    def test_bringUmbrella(self):
        self.assertEqual(bringUmbrella(50), True)

    def test_bringUmbrella2(self):
        self.assertEqual(bringUmbrella(40), False)


unittest.main(argv=[''], verbosity=2, exit=False)