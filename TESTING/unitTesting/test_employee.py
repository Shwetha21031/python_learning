import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) :
    #     print('setup class')

    # @classmethod
    # def tearDownClass(cls):
    #     print('teardown class called')

    def setUp(self):
        # print('setup called')
        self.emp_1 = Employee('Eren','Jeager',10000)
        self.emp_2 = Employee('Mikasa','Ackremen',20000)
    def tearDown(self):
        # print('terdown called')
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email,'Eren.Jeager@email.com')
        self.assertEqual(self.emp_2.email,'Mikasa.Ackremen@email.com')

        self.emp_2.last = 'Jeager'
        self.assertEqual(self.emp_2.email,'Mikasa.Jeager@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullName,'Eren Jeager')
        self.assertEqual(self.emp_2.fullName,'Mikasa Ackremen')

        self.emp_1.first = 'eren'
        self.emp_2.last = 'Jeager'

        self.assertEqual(self.emp_1.fullName,'eren Jeager')
        self.assertEqual(self.emp_2.fullName,'Mikasa Jeager')


    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay,10500)
        self.assertEqual(self.emp_2.pay,21000)

    # def test_monthly_schedule(self):
    #     with patch('employee.requests.get') as mocked_get:
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value.text = 'Success'

    #         schedule = self.emp_1.monthly_schedule('May')
    #         mocked_get.assert_called_with('http://company.com/Jeager/May')
    #         self.assertEqual(schedule,'Success')




if __name__ == 'main':
    unittest.main()