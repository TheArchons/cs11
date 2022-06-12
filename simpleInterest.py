print("Which would you like to solve for?")
print("1. Principle")
print("2. Simple interest")
print("3. Rate")
print("4. Time")
print("5. Compound interest")

choice = input("Enter your choice: ")

if choice == "1": # Principle
    interest = float(input("Enter the interest: ")) # conversion to float to perform math
    rate = float(input("Enter the rate per year as a percentage: ").replace("%", ""))/100 # replace removes any percent symbols from the input
    time = float(input("Enter the time in years: "))
    print("The principle is: $", format(round(interest/(rate*time), 2), ".2f")) # round to 2 decimal places and force 2 decimal places
elif choice == "2": # Simple interest
    principle = float(input("Enter the principle: "))
    rate = float(input("Enter the rate per year as a percentage: ").replace("%", ""))/100
    time = float(input("Enter the time in years: "))
    print("The interest is: $", format(round(principle*rate*time, 2), ".2f"))
elif choice == "3": # Rate
    principle = float(input("Enter the principle: "))
    interest = float(input("Enter the interest: "))
    time = float(input("Enter the time in years: "))
    print("The rate is: " + str(round(interest/(principle*time), 2)*100) + "%") # multiply by 100 to convert from a decimal to a percent
elif choice == "4": # Time
    principle = float(input("Enter the principle: "))
    interest = float(input("Enter the interest "))
    rate = float(input("Enter the rate per year as a percentage: ").replace("%", ""))/100
    print("The time is: ", interest/(principle*rate), "years")
elif choice == "5": # Compound interest
    principle = float(input("Enter the principle: "))
    rate = float(input("Enter the rate per year as a percentage: ").replace("%", ""))/100
    time = float(input("Enter the time in years: "))
    print("The compound interest is: $", format(round((principle*(1+rate)**time)-principle, 2), ".2f")) # Amount of money excluding the principle
    print("The total amount is: $", format(round(principle*((1+rate)**time), 2), ".2f")) # Amount of money including the principle
else: # Invalid choice
    print("Invalid choice.")