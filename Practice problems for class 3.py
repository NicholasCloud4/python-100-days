#Conditional Example
a = 7
c = 9
a = 4
if a > 6:
    b = 9
else:
    b = 10

if a > 7:
    d = 3
if a > 3:
    d = 2
else:
    d = 1
# What are the values of a, b, c, and d?
# a = 4
# b = 10
# c = 9
# d = 2



# Spot the Difference
# Here are three different pieces of code:

# Code A

# x = int(input("Enter a number: "))

# if x > 0:
#     print("x is positive")
# else:
#     if x < 0:
#         print("x is negative")
#     else:
#         print("x is zero")


# # Code B
# x = int(input("Enter a number: "))

# if x > 0:
#     print("x is positive")
# elif x < 0:
#     print("x is negative")
# else:
#     print("x is zero")


# # Code C 
# x = int(input("Enter a number: "))

# if x > 0:
#     print("x is positive")
# if x < 0:
#     print("x is negative")
# else:
#     print("x is zero")



# What if you enter 10 as x? What is the output for code A, B, C?
# A = positive, B = positive, C = positive, zero

# What if you enter 0 as x? What is the output for code A, B, C?
# A = zero, B = zero, C = zero

# What is the difference between A and B?
# What is the difference between A and C?
# What is the difference between B and C?
# Between A and B, which piece of code is more readible?




# Suppose we want a piece of code that allows you to take in some user-input number 
# (use this: x = int(input("Enter a number: "))) and output whether the code is 
# even, odd, or zero. Implement this.

x = int(input("Enter a number: "))

if x % 2 == 0:
    print("x is even")
elif x % 2 == 1:
    print("x is odd")
else:
    print("x is zero")



# Suppose we are given three numbers x, y, and z. 
# Write a piece of code that will print the largest of the three numbers 
# (for ex: if x=1, y=10, and z=-2.3, the code should print 10).

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z)

