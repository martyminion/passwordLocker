
class User:
  '''
  this class generates new instances of a user
  '''
  Users = []

  def __init__(self, firstname, lastname, age, email, username):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.email = email
    self.username = email
  