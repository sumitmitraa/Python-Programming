# Write a python program that prompts the user to input a city and dislay thte famous monument of that city.

# Mumbai: Gateway of India
# Kolkata: Victoria Memorial 
# Chennei: Marina Beach
# Banglore: Botanical Garden
# Pune: Shaniwar Wada

city_name = input('Enter the name of city:')

if city_name == 'Mumbai':
  print('Famous Momument is Gateway of India')
elif city_name == 'Kolkata':
  print('Famous Momument is Victoria Memorial')
elif city_name == 'Chennei':
  print('Famous Momument is Marina Beach')
elif city_name == 'Banglore':
  print('Famous Momument is Botanical Garden')
elif city_name == 'Pune':
  print('Famous Momument is Shaniwar Wada')
else:
  print('City Not Found')