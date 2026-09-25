print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

if people == 1:
    total_bill = bill * tip / 100 + bill
    print(f"Total bill for one person is: ${total_bill:.2f}")
else:
    total_bill = (bill * tip / 100 + bill) / people
    print(f"Total bill for each person is: ${total_bill:.2f}")
    