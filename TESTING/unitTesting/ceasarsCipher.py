import unittest
import string


# production code
def encrypt(message):
    abc = string.ascii_letters + string.digits + string.punctuation + " "
    # print(abc)
    encrypted_message = "".join([abc[abc.find(char)+1] if len(abc) > (abc.find(char)+1) else abc[0] for i,char in enumerate(message)])
    return encrypted_message



# encapsulate all the future test in this class , must inherit unittest class
# assertions aka messages
class TestEncryption(unittest.TestCase): 
# body will consist of all the tests
    def setUp(self): # in general we initialize inside __init__ method , in testcase class we initialize inside setUp method
        self.my_message = 'holaa papi 888'

# first portion of test method must be "test_"
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    def test_inputType(self):
        self.assertIsInstance(self.my_message,str)

    def test_functionReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))

    def test_lenIO(self):
        self.assertEqual(len(self.my_message),len(encrypt(self.my_message)))

    def test_differentIO(self):
        self.assertNotIn(self.my_message,encrypt(self.my_message))
    
    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message),str)

    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.digits + string.punctuation + ''
        encrypted_msg = "".join([abc[abc.find(char)+1] for i,char in enumerate(self.my_message)])
        self.assertEqual(encrypted_msg,encrypt(self.my_message))

    
if __name__ == '__main__':
    unittest.main()