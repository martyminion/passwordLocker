
class User:
  '''
  this class generates new instances of a user
  '''
  users_list = []

  def __init__(self, firstname, lastname, age, email, password):
    '''
    initializes the instances of user
    '''
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.email = email
    self.password = password
  
  def save_users(self):
    '''
    saves the users into the lisr of users
    '''
    User.users_list.append(self)
  @classmethod
  def check_email_password_match(cls,useremail,userpassword):
    '''
    checks if password and email match
    '''

    for user in cls.users_list:
      if user.email == useremail and user.password == userpassword:
        return True
    return False
  

  
