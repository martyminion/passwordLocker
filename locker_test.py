import unittest
from User import User
from Credentials import Credentials

class TestLocker(unittest.TestCase):
  '''
  this class defines the tests to be run on the user and credentials classes
  parameters passed:
  unittest.TestCase is a class that helps in creating the test cases
  '''

  def setUp(self):
    '''
    the setup is a method that runs before each of the test cases is run
    creates a test user and his credentials
    '''
    self.new_user = User("Michael","Cotts",25,"mchcots@gmail.com","mchcots")
    self.new_credentials = Credentials("mchcots","qwerty123")

  def test_init(self):
    '''
    tests if the users and credentials have been initialized correctly
    '''
    self.assertEqual(self.new_user.firstname,"Michael")
    self.assertEqual(self.new_user.lastname,"Cotts")
    self.assertEqual(self.new_user.age,25)
    self.assertEqual(self.new_user.email,"mchcots@gmail.com")
    self.assertEqual(self.new_user.username,"mchcots")

    self.assertEqual(self.new_credentials.username,"mchcots")
    self.assertEqual(self.new_credentials.password,"qwerty123")

if __name__ == '__main__':
  unittest.main()