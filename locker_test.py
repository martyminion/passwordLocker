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
  