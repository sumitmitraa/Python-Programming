# Temprature convenient or not

temp = float(input('Enter the Temprature:'))

if temp <= 15:
  print('Temprature is not convenient.')
elif 24 < temp < 28:
  print('Temprature is convenient.')
else:
  print('Temprature is high.')