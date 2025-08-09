# You are working on a project to analyze stock market data, Create variables to store the stock symbol, current price, and percentage change in price.
 
# Than claculate the new price after a 10% increase using arthematic operators.

# Finally prompt the user to enter thier budget, convert it into a float and compare it with new price.

stock_symbol = 'xyz'
current_price = 150
percent_chage = 10

new_price = current_price*(1+percent_chage/100)

print('the new price is ',new_price)

user_budget = float(input('Enter your budget:'))
compare = user_budget >= new_price

print('is user budget is greater than new price:',compare)