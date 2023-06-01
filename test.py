
import main
import unittest

class TestMain(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(main.addition(1, 2), 3, "should be 3")
        self.assertEqual(main.addition(5, 5), 10, "should be 10")
        self.assertEqual(main.addition(40, 20), 60, "should be 60")
        self.assertEqual(main.addition(-3, 2), -1, "should be -1")

    def test_subtraction(self):
        self.assertEqual(main.subtraction(8, 2), 6, "should be 6")
        self.assertEqual(main.subtraction(5, 5), 0, "should be 0")
        self.assertEqual(main.subtraction(40, 20), 20, "should be 20")
        self.assertEqual(main.subtraction(-3, 2), -5, "should be -5")

if __name__ =='__main__':
    unittest.main()
