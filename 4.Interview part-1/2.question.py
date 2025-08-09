# Ask the user 1 & 2 to enter house size, number of rooms they want and, check the data type user has entered.

# Calculate the price of house if per sq. feet is rs. 5000

# Threshold price is 75lakh rs., which user is paying the price above threshlod price.


print('For user 1')
house_size_1 = float(input('Enter the size you want (in sq. feet):'))
bedroom_1 = int(input('Enter the no. of badroom you want:'))
budget_1 = float(input('Enter your budget:'))

print('For user 2')
house_size_2 = float(input('Enter the size you want (in sq. feet):'))
bedroom_2 = int(input('Enter the no. of badroom you want:'))
budget_2 = float(input('Enter your budget:'))

house_price_1 = house_size_1*5000
house_price_2 = house_size_2*5000

print('The price of house for user 1 is ',house_price_1)
print('The price of house for user 2 is ',house_price_2)

threshold = 7500000
user_1_threshold = house_price_1 >= threshold 
user_2_threshold = house_price_2 >= threshold 

print('User 1 is paying above threshold:',user_1_threshold)
print('User 2 is paying above threshold:',user_2_threshold)
