# Practice problems for class 2

# x = [1.1, 2, [3, 'tomato', 4], 'cat']
# print(x)
# What type is x? It is a list
# What type is x[0]? It is a float
# What type is x[2]? It is a list
# What type is x[-1]? It is a string
# What is the value of x[2][2]? It is 4
# What is the value of x[2][-1]? It is 4
# What is the value of x[-1][2]? Letter 't'
# What is the value of x[4]? Error
# Let's say I run this line: x[1] = 'hi'. Now what is x[1]? It is 'hi'
# What is the value of x now? [1.1, 'hi', [3, 'tomato', 4], 'cat']
# Let's say you want to add you name to the end of x. What is the command you need to do this? x.append('Name')



# tup = (1, 2, "c")
# What type is tup? It is a tuple
# What happens if I run tup[0] = "a"? It cannot work because it is immutable. Would get a type error.
# Let's say you want to add you name to the end of tup. Can you do this?

# This is a trick question. You cannot append to the tuple like we did above for the string. 
# Python will give you an error if you try to do that. 
# However, one way we can get around this is to create a NEW tuple with your name, 
# and then set tup equal to that new variable: 
# tup = (1, 2, "c", "kylie") or tup = tup + ("kylie",) (("kylie",) is a tuple with only 1 value in it).



# What is the value of [1, 2]+[3,4]*2? [1, 2, 3, 4, 3, 4]
# What is the value of ['b'] + ['a' + 'n']*2 + ['a']? [b, an, an, a]
# What is the value of "na"*8 + " batman"? nananananananana batman


#More slicing
# In Python, we can also take "slices" of sequences (strings, tuples, lists). 
# Let's say sentence = "Hello World!". We can take sub-sequences of this word like this:

# sentence[0:4]  # gives us the first 4 characters --> "sent"
# sentence[:4]  # also gives us "sent"
# sentence[6:]  # gives us the remainder of the sentence starting from index 6 ("W") --> "World!"
# sentence[2:5] # gives us indices 2, 3, 4 of the string --> "llo"
# Here are some exercises:

# hello = "Hello World"
# name = "Lisa"

# print(hello[0:5], name)

# What does name[3:] give you? a
# What does hello[1:5] give you? ello
# What does hello[0:8:2] give you? Hello Wo
# What does name[0:-2] give you? #Li
# What does hello[-3:] give you? #rld
# We want to write "Hello Lisa" using these strings above. How do I do that?
#print(hello[0:5], name)


# Let's pretend we're about to go on vacation to Spain. 
# BUT, we don't know Spanish! Let's use our computer to translate for us. 
# Write a short script that will let you input a number in English (zero-nine), 
# and it should output the Spanish translation.

# print(input("Enter a number from 0 to 9: "))

spanish_translator = {
    "0": "cero",
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve",
}

number = input("Enter a number from 0 to 9: ")
print(spanish_translator[number])