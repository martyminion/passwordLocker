
import random
import string
from User import User
from Credentials import Credentials


def create_new_user(first_name, last_name, user_age, user_email,user_pasword):
  '''
  creates a new instance of a user
  '''
  new_user = User(first_name, last_name, user_age, user_email,user_pasword)

  return new_user

def save_user(user):
  '''
  saves the instance of the user
  '''
  user.save_users()

def email_password_match(useremail,userpassword):
  '''
  checks if the username used and password match that of the username
  '''
  return User.check_email_password_match(useremail,userpassword)

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

def save_account(account):
  '''
  saves the instance of the account
  '''
  account.save_credentials()

def search_account(account_name):
  '''
  searches for the inputed account name
  '''
  return Credentials.search_account(account_name)

def display_accounts():
  '''
  displays all the available Accounts and credentials
  '''
  return display_accounts()

def autogenerate_password(password_length):
  '''
  generates a password from alphanumenric  characters
  '''
  character_pool = string.ascii_letters + string.digits
  return "".join((random.choice(character_pool) for i in range(password_length)))

def main():
  print("Welcome to Password Locker, to Sign up: \n Please Enter you first name")
  fname = input()
  print("Please enter your last name \n")
  lname = input()
  print("Please enter you age in numbers \n")
  users_age = int(input())
  print("Please Enter email we can contact you on \n")
  users_email = input()
  print("Please Enter a password")
  users_password = input()

  save_user(create_new_user(fname, lname, users_age, users_email,users_password))

  print(f"Thank you {fname} {lname} for signing up")
  print("--" * 20)

  print("Log in to Password Locker")
  print("Email ......")
  logemail = input()
  print("Password .........")
  logpassword = input()

  result = email_password_match(logemail,logpassword)

  while result == True:
    print("Thank you for using Password Locker")
    print("What would you like to do:\n A: Add a new Account \n B: Display current accounts \n C: Search for existing account \n D: Delete an account \n E: End Program")
    print("Please choose options using the preceding Letter, A to Add a new account")
    choice = str(input()).capitalize()

    if choice == "A":
      print("Type 1: To Enter credentials of an existing acount \n Type 2: To Enter credentials of a completely new acount")
      new_account_choice = input()
      if new_account_choice == "1":
        print("Please Enter Account Name")
        new_account_name = input()
        print("Please Enter Account User Name")
        new_account_username = input()
        print("Please Enter Account Password")
        new_account_password = input()

        print(f"Account name:{new_account_name} \n Account Username: {new_account_username} \n Account Password: {new_account_password} \n")

        save_account(create_new_account_credentials(new_account_name, new_account_username, new_account_password))
      elif new_account_choice == "2":
        print("Please Enter Account Name")
        new_account_name = input()
        print("Please Enter Account User Name")
        new_account_username = input()
        print("Enter YES for an autogenerated password or NO to create your own password")
        password_choice = input().capitalize()
        if password_choice == "YES":
          print("How many character does the password need to be")
          pass_length = int(input())
          new_account_password = autogenerate_password(pass_length)
          print(new_account_password)

        elif password_choice == "NO":
          print("Please Enter Account Password")
          new_account_password = input()

        print(f"Account name:{new_account_name} \n Account Username: {new_account_username} \n Account Password: {new_account_password} \n")

        save_account(create_new_account_credentials(new_account_name, new_account_username, new_account_password))

    elif choice == "B":
      if display_accounts():
        print("Current Accounts \n")

        for account in display_accounts():
          print(f"{account.account} {account.username} {account.password} \n")
      
      else:
        print("You have no accounts yet")
    elif choice == "C":
      print("Enter account name to search for")
      account_search = input()

      if search_account(account_search):
        account_result = search_account(account_search)
        print(f"{account_result.account} {account_result.username}{account_result.password}")

      else:
        print("You do not have search an account")

    elif choice == "D":
      print("Enter account name to delete")
      delete_account_name = input()

      account_delete = search_account(delete_account_name)
      delete_account(account_delete)
    elif choice == "E":
      print("Thank you for using Password Locker")
      break
    else:
      print("Please Choose an option from the available options")
      
if __name__ == '__main__':
  main()







