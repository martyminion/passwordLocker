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
    self.new_user = User("Michael","Cotts",25,"mchcots@gmail.com","zxcv456")
    self.new_credentials = Credentials("twitter","mchcots","qwerty123")

  def tearDown(self):
    '''
    this method does a clean up after each test case is run
    clears the credential list and user list
    '''
    User.users_list = []
    Credentials.credentials_list = []

  def test_init(self):
    '''
    tests if the users and credentials have been initialized correctly
    '''
    self.assertEqual(self.new_user.firstname,"Michael")
    self.assertEqual(self.new_user.lastname,"Cotts")
    self.assertEqual(self.new_user.age,25)
    self.assertEqual(self.new_user.email,"mchcots@gmail.com")
    self.assertEqual(self.new_user.password,"zxcv456")
    
    self.assertEqual(self.new_credentials.account,"twitter")
    self.assertEqual(self.new_credentials.username,"mchcots")
    self.assertEqual(self.new_credentials.password,"qwerty123")

  def test_save_user_credentials(self):
    '''
    tests if the methodsto save in the different classes work
    '''
    self.new_user.save_users()
    self.new_credentials.save_credentials()

    self.assertEqual(len(Credentials.credentials_list),1)
    self.assertEqual(1,len(User.users_list))
  
  def test_save_multiple_users_credentials(self):
    '''
    tests if we can save multiple users and credentials
    '''
    self.new_user.save_users()
    self.new_credentials.save_credentials()
    dummy_user = User("Mia","Hulfsen",21,"hulfmia@gmail","lkjh987")
    dummy_credentials = Credentials("facebook","miahulf","asdfg456")
    dummy_user.save_users()
    dummy_credentials.save_credentials()

    self.assertEqual(len(User.users_list),2)
    self.assertEqual(len(Credentials.credentials_list),2)
  
  def test_displayCredentials(self):
    '''
    tests if the list of credentials is displayed
    '''
    self.assertEqual(Credentials.display_accounts(),Credentials.credentials_list)

  def test_search_account(self):
    '''
    tests if you can search for a particular account
    '''
    self.new_credentials.save_credentials()
    dummy_credentials = Credentials("facebook","miahulf","asdfg456")
    dummy_credentials.save_credentials()

    account_exist = Credentials.search_account("facebook")
    self.assertTrue(account_exist)
    account_notexist = Credentials.search_account("instagram")
    self.assertFalse(account_notexist)

  def test_delete_account(self):
    '''
    tests if the account can be deleted
    '''
    self.new_credentials.save_credentials()
    dummy_credentials = Credentials("facebook","miahulf","asdfg456")
    dummy_credentials.save_credentials()

    Credentials.credentials_list.remove(dummy_credentials)
    self.assertEqual(1,len(Credentials.credentials_list))






if __name__ == '__main__':
  unittest.main()