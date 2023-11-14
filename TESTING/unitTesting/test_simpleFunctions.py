import unittest
import simpleFunctions

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = simpleFunctions.add(10,5)
        self.assertEqual(result,15)
        self.assertEqual(simpleFunctions.add(-1,-1),-2)
        self.assertEqual(simpleFunctions.add(-1,+1),0)

    def test_sub(self):
        self.assertEqual(simpleFunctions.sub(5,0),5)
        self.assertEqual(simpleFunctions.sub(10,-2),12)
        self.assertEqual(simpleFunctions.sub(-5,10),-15)

    def test_mul(self):
        self.assertEqual(simpleFunctions.mul(10,5),50)
        self.assertEqual(simpleFunctions.mul(-2,-2),4)
        self.assertEqual(simpleFunctions.mul(-5,0.5),-2.5)

    def test_div(self):
        self.assertEqual(simpleFunctions.div(10,-5),-2.0)
        self.assertEqual(simpleFunctions.div(5,2),2.5)
        self.assertEqual(simpleFunctions.div(-10,-10),1)

        self.assertRaises(ValueError,simpleFunctions.div , 10,0)

        with self.assertRaises(ValueError): #with context manager
            simpleFunctions.div(5,0)

if __name__  == '__main__':
    unittest.main()