# Practice problems for class 1
#For each of the following, determine what the type of the value is

# 1
True   #boolean or bool

# 2
2.99   #float

# 3
None   #None

# 4
3      #Integer

# 5
3.     #float

# 6
0      #Integer

# What about these combinations?
# 7
3. + 1      # float

# 8
25 - 16.   # float

# 9
-5 - 15    # integer

# 10
32 > 335   # boolean

# 11
94.2 == 35 # boolean

# 12
4 == 4.    # boolean

# 13
34 / 322   # float

# 14
322 % 34   # integer


# Entangling strings and numbers
# What would 7+8 produce?
#  It would produce 15.

# What about 7.+8? How is this result different from the one above?
# It would produce 15.0. The result is different from the one above becuase it is of float type.

# What would happen if we tried 7+"8"?
# It would produce an error.

# What about "7"+"8"?
# It would produce "78".


# Converting Between Types
# What is the type (ex: integer, float, string, etc) and value (ex: 0, 3.14, "a", etc) of the result? 
# Or is there an error?

# # 19
# print(int(7.8), type(int(7.8)))


# # 20
# print(float(6), type(float(6)))  


# # 21
# print(str(6.0), type(str(6.0)))


# # 22
# print(int("2"), type(int("2")))

# # 23
# print(float("7.8"), type(float("7.8")))

# # 24
# int("tomato") # Error

# # 25
# int("7.8") # Error

# # 26
# print(float("6"), type(float("6")))

# Operators Practice

# 27
5 + 3 - 16
# -8

# 28
25 // 4
# 6

# 29
8+4*2   
#16     

# 30
(8+4)*2   
#24     

# 31
3 ** 5         
#243

# 32
3.0 ** 5     
#243.0  

# 33
3/2      
#1.5      

# 34
16.3 % 16     
#0.30000000000000004 

# 35
True or False       
# True 

# 36
True and False    
# False

# 37
3 > 4 or 3 == 3  
# True 

# 38
not False      
# True  

# 39
not (4 > 3 and 100 > 6)    
#False

# 40
4 == 2 + 2        
# True

# What if we make x = 1 and then executed x = x+5? 
# Do you think this is allowed? If so, what would x be equal to?

# Yes it is allowed. x = 6


# What is new_amount equal to after executing this piece of code?
amount = 3
amount - 5.3
new_amount = amount + 8.8
print(new_amount)
# new_amount is equal to 11.8 because the second line (amount - 5.3) 
# did not actually set the variable amount to anything.


# 43
# Write some code to set pi equal to 3.14, r equal to 10, and area equal to pi times r squared.
pi = 3.14
r = 10
area = pi * r**2

