# User is eligible or not for vote

age = int(input('Enter your age:'))
if age >= 18:
  print('You are eligible for vote')
elif age <= 0 :
  print('Age is not valid')
else:
  print('You are not eligible for vote')
