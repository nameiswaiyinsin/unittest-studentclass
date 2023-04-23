import unittest
from student import Student
from datetime import timedelta


class TestStudent(unittest.TestCase):
    """
    * Code Along challenge
    * Create a new test method called test_apply_extension in test_student.py file
    * Inside test_apply_extension, store the current end_date for our student instance in a variable called old_end_date
    * Call a method named apply_extension that will take a number of days as an argument on the student instance to update the end_date
    * Assert whether the instance's end_date equals the old end date plus the days argument that was passed in using timedelta
    * Import timedelta fromo datetime (as seen on line 3)
    * Run the tests to confirm that the new method is failing (python3 test_student.py in terminal) because the apply_extension() method hasnt been created yetr in the Student class in student.py file
    * In the Student class, create a new method called apply_extension that has a parameter called days
    * Use the timedelta method from datetime to update the end_date property
    * Run the test to confirm they are working. (type python3 test_student.py in terminal)
    """

    # @classmethod
    # def setUpClass(cls):
    #     print('setUpClass')

    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass')


    def setUp(self):
        print('setUp')
        self.student = Student("John", "Doe")


    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, "john.doe@email.com")

    
    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

        """
        The method below is also great!  But keep in mid that  it will
        only be correct if a student has received 1 extenstion.  If 
        they receive a second - it would return false

        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, self.student._start_date + timedelta(days=370))
        """


if __name__ == "__main__":
    unittest.main()