# While Loop Question ...

# Validating user email addresses
# Use a while loop to iterate through the input and check if the email address contains an "@" symbol and an "." symbol.

email = input('Enter your mail id:')

valid_email = False

while not valid_email:
  if '@' in email and '.' in email :
    print('Email id is validate')
    valid_email = True
  else:
    print('Email id is not validate')
    email = input('Please enter your valid email id:')
