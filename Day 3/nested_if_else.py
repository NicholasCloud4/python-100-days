print("Welcome to the ride!")
height = int(input("Enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Middle age tickets are $0.")
        bill = 0
    else:
        print("Adult tickets are $12.")
        bill = 12

    photo = input("Would you like to have your photo taken? It is an extra $3. (yes/no): ")
    if photo.lower() == "yes":
        print("Your photo will be taken.")
        bill += 3
    else:
        print("You chose not to have your photo taken.")

    print(f"Your total bill is ${bill}.")

else:
    print("Sorry, you have to be at least 120 cm tall to ride.")