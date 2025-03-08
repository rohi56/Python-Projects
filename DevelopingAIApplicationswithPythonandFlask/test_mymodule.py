#program for unit testing of mymodule.py
import unittest
from mymodule import Square, Addition

class TestSquare(unittest.TestCase):
    def test_square(self):
        c1 = Square(5)
        self.assertEqual(c1.square(), 25)
    
    def test_double(self):
        c1 = Square(5)
        self.assertEqual(c1.double(), 10)
        
class TestAddition(unittest.TestCase):
    def test_add(self):
        c1 = Addition(5, 10)
        self.assertEqual(c1.add(), 15)
    
if __name__ == '__main__':
    unittest.main()