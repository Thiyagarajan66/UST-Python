import re

email = input("enter the email: ")
pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

def check(email):
   if re.match(pattern,email):
      return "entered email is valid one"
   return "entered email is not valid one"
print(check(email)) 





