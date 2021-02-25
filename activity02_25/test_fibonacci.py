import unittest
import fibonacci

class TestFibonacciCalculator(unittest.TestCase):
   def test_1(self):
      result = fibonacci.calc_fibo(3)
      self.assertEqual(result, 2)

   def test_2(self):
      result = fibonacci.calc_fibo(0)
      self.assertEqual(result, 0)
      
   def test_3(self):
      result = fibonacci.calc_fibo(6)
      self.assertEqual(result, 8)

if __name__ == "__main__":
   unittest.main(verbosity=2)
