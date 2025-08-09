# Q.Implement a python program to generate the multiplication table of a given number using a for loop.


num = int(input('Enter a number to generate its table:'))
print('The multiplication table of',num)

for i in range(1,11):
  print(f"{num} x {i} = {num*i}")

 