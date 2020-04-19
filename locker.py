
import random
from User import User
from Credentials import Credentials


def create_new_user(first_name, last_name, user_age, user_email,user_pasword):
  '''
  creates a new instance of a user
  '''
  new_user = User(first_name, last_name, user_age, user_email,)

  return new_user
user_pasword
def save_user(user):
  '''
  saves the instance of the user
  '''
  user.save_users()

def create_new_account_credentials(account_name, account_username, account_password):
  '''
  creates a new credentials instance
  '''
  new_credentials = Credentials(account_name, account_username, account_password)
  
  return new_credentials

def delete_account(account):
  '''
  deletes the instance of the account
  '''
  account.delete_account()

def save_account(account);
  '''
  saves the instance of the account
  '''
  account.save_credentials()

def search_account(account_name):
  '''
  checks if the account exists
  '''
  return Credentials.search_account(account_name)


def main():
  print("Welcome to Password Locker \n Please Enter you first name")
  fname = input()
  print("Please enter your last name \n")
  lname = imput()
  print("Please enter you age in numbers \n")
  users_age = int(input())
  print("Please Enter email we can contact you on \n")
  users_email = input()
  print("Please Enter a password")
  users_password = input()

  save_user(create_new_user(fname, lname, users_age, users_email,users_password))



