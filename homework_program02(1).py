# Homework Program 02
# In this assignment I made a program that calculates gas mileage and the cost of a tank of gas for a car.

# The reason why I typed "Welcome! What is your name?"so that the user feels welcomed with my program right from the start.
print("Welcome! What is your name? ")
message = input()

# After each input, I wanted to print them so the program and user can read what was typed for each answer.
# Below the print I decided to add the float since I will be using the inputs later for the equations.
distance_traveled = input("Hello, please enter the distance traveled: ")
print(distance_traveled)
dt = float(distance_traveled)

tank_gallons = input("Please enter the size of tank in gallons: ")
print(tank_gallons)
tg = float(tank_gallons)

price_gallon = input("Please enter the price of gallon of gas: ")
print(price_gallon)
pg = float(price_gallon)

# For the equations, I used the variables from each float to get the dividing and multiplication outcome.
# That is how I was able to get the total of gas mileage and cost.
# Each time a user inputs their information, they will get an estimate of the gas mileage and cost.
print("The gas mileage is: ")
print(dt / tg)
print("The cost is: ")
print(tg * pg)

# I decided to thank the user for taking time out of their day to help input personal data into my program.
end_mes = input("Thank you. Have a nice day!")
