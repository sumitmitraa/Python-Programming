# You are tasked with developing a python program to manage employee salaries for a company. Your porgram should claculate the net salary of each employee based on thier base salary, deduction, and bonuses. Additionally, employee who have been with the company for more than 5 years are eligible for an additional loyalty bonus, 8% of salary. Deductions of tax will be 12%.

base_salary = float(input('Enter your base salary:'))
year_of_services = int(input('Enter your years of services:'))

if year_of_services >= 5:
  total_salary = base_salary + (0.08*base_salary) - (0.12*base_salary)
  print('You will get net salary',total_salary)
else:
  net_salary = base_salary - (0.12*base_salary)
  print('Your net salary is',net_salary)
