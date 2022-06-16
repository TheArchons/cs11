# asks the user for a number of pennies to replace
pennyCount = int(input("How many pennies do you have? "))

# Create a list of pennyCount pennies
pennies = []
for i in range(0, pennyCount):
    pennies.append(1)

#replace every other penny with a 5
for i in range(1, len(pennies), 2):
    pennies[i] = 5

#replace every third penny with a 10
for i in range(2, len(pennies), 3):
    pennies[i] = 10

#replace every fourth penny with a 25
for i in range(3, len(pennies), 4):
    pennies[i] = 25

print("The total amount of money on the table is ${}".format(sum(pennies)/100)) # takes the sum of the list and divides by 100 to get the total amount of money