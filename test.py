from Credentials import Credentials

def search_account(account_name):
  '''
  checks if the account exists
  '''
  return Credentials.search_account(account_name)
def create_new_account_credentials(account_name, account_username, account_password):
  '''
  creates a new credentials instance
  '''
  new_credentials = Credentials(account_name, account_username, account_password)
  
  return new_credentials

def save_account(account):
  '''
  saves the instance of the account
  '''
  account.save_credentials()

def main():
  save_account(create_new_account_credentials("twitter", "andrew", "ytrt789"))
  save_account(create_new_account_credentials("facebook", "james", "dfgfdg789"))
 
  print("Please Enter a name")
  searchname = input()

  result = search_account(searchname)
  for account in Credentials.credentials_list:
    if account.account == result:
       return account

  print(f"{account.account} {account.username}")

if __name__ == '__main__':
  main()

