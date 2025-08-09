# Create variable to store current temperature . the min temperature recored and max temperature recored.

# get temperature from user and determine temp is within range of min and max temp

current_temp = float(input('Enter Temperatuer of your City:'))
min_temp = 25
max_temp = 40

normal_temp = min_temp <= current_temp <= max_temp
print('is Temperatuer normal:',normal_temp)