class Credentials:
  '''
  this class generates the instances of the users credentials
  '''
  credentials_list = []

  def __init__(self, username, password):
    '''
    initalizes the instances of credentials
    '''
    self.username = username
    self.password = password

  def save_credentials(self):
    '''
    saves the credentials into an array
    '''
    Credentials.credentials_list.append(self)