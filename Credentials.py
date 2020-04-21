import pyperclip

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

  def delete_account(self):
    '''
    deletes an unused account by users choice
    '''
    Credentials.credentials_list.remove(self)
    
  @classmethod
  def search_account(cls,account_name):
    '''
    searches if there exists the searched account
    '''
    for single_account in cls.credentials_list:
      if single_account.account == account_name:
        return single_account

  @classmethod
  def display_accounts(cls):
    '''
    displays all the accounts and their details
    '''
    return cls.credentials_list

  @classmethod
  def copy_password(cls,account_name):
    '''
    copys the account password
    '''
    account_found=Credentials.search_account(account_name)
    pyperclip.copy(account_found.password)