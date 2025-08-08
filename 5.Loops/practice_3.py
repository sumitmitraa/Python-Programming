# ek python program likhna hai jisme user se puchna hai ki usne kitna saman kharida hai. User ko har saman ka price dalne bolna hai. 

# agar sab saman ka total 1000 se uper aata hai to user to total price pe 10% discout dena hai.

# agar sab saman ka total 500 se 1000 ke bich hai to user to total price pe 5% discout dena hai.

# total price 500 se kam hone pe koi discount nhi dena hai.


num_items = int(input('Enter number of items purchased:'))
total_price = 0

for i in range(1,num_items+1):
  
  single_price = float(input(f'Enter the price of {i} item:'))
  total_price = total_price + single_price

print(f'Total price of {i} items is {total_price}')

if total_price >= 1000:
  discount_10 = 0.1*total_price
  print("Congratulation you got '10%' discount")
  print(f'After discount your price is {total_price - discount_10}')

elif 500 <= total_price < 1000:
  discount_5 = 0.05*total_price
  print("Congratulation you got '5%' discount")
  print(f'After discount your price is {total_price - discount_5}')

else:
  print("Sorry you have no discount")
  print(f'It is Same {total_price}')
