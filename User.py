
class User:
  '''
  this class generates new instances of a user
  '''
  users_list = []

  def __init__(self, firstname, lastname, age, email, username):
    '''
    initializes the instances of user
    '''
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.email = email
    self.username = username
  
  def save_users(self):
    '''
    saves the users into the lisr of users
    '''
    User.users_list.append(self)
