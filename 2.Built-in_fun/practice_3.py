# Calculate BMR (Basal Metabolic Rate)
# BMR Formula = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

# age hamesha positive hoti h isliye abs() function ka use kiya 

age = abs(int(input('Enter your age:')))       
weight = float(input('Enter your weight (in kg):'))
height = float(input('Enter your height (in cm):'))

BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
print('Your BMR is',int(BMR))