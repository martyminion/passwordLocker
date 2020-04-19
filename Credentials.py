class Credentials:
  '''
  this class generates the instances of the users credentials
  '''
  credentials_list = []

  def __init__(self, account, username, password):
    '''
    initalizes the instances of credentials
    '''
    self.account = account
    self.username = username
    self.password = password

  def save_credentials(self):
    '''
    saves the credentials into an array
    '''
    Credentials.credentials_list.append(self)
  @classmethod
  def display_accounts(cls):
    '''
    displays all the accounts and their details
    '''
    return cls.credentials_list

  @classmethod
  def search_account(cls,account_name):
    '''
    searches if there exists