# Learning Python Dictionaries
# Run this file and read the output alongside the code.

# ---------------------------------------------------------------
# 1. What is a dictionary?
# ---------------------------------------------------------------
# A dictionary stores data as key: value pairs.
# You look things up by KEY (like a word in a real dictionary).
programming_dictionary = {
    "Bug": "An error in a program that prevents it from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
print("1. Whole dictionary:", programming_dictionary)

# ---------------------------------------------------------------
# 2. Getting values
# ---------------------------------------------------------------
print("\n2. Getting values")
print(programming_dictionary["Bug"])

# Using a key that doesn't exist raises a KeyError:
# print(programming_dictionary["Loop"])   # <- uncomment to see the error

# .get() is safer: returns None (or a default you choose) instead of crashing
print(programming_dictionary.get("Loop"))
print(programming_dictionary.get("Loop", "Not defined yet"))

# ---------------------------------------------------------------
# 3. Adding and changing items
# ---------------------------------------------------------------
print("\n3. Adding and changing items")
programming_dictionary["Loop"] = "The action of doing something over and over again."
print("After adding Loop:", list(programming_dictionary.keys()))

programming_dictionary["Bug"] = "A moth in your computer."  # same key = overwrite
print("Bug is now:", programming_dictionary["Bug"])

# ---------------------------------------------------------------
# 4. Removing items
# ---------------------------------------------------------------
print("\n4. Removing items")
del programming_dictionary["Loop"]
print("After deleting Loop:", list(programming_dictionary.keys()))

removed = programming_dictionary.pop("Function")  # removes AND returns the value
print("Popped:", removed)
print("Remaining:", programming_dictionary)

# Wipe the whole dictionary
programming_dictionary.clear()
print("After clear:", programming_dictionary)

# ---------------------------------------------------------------
# 5. Looping through a dictionary
# ---------------------------------------------------------------
print("\n5. Looping")
student_scores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74}

for name in student_scores:  # looping gives you the KEYS
    print(name, "->", student_scores[name])

for name, score in student_scores.items():  # keys AND values together
    print(f"{name} scored {score}")

print("Keys:  ", list(student_scores.keys()))
print("Values:", list(student_scores.values()))

# ---------------------------------------------------------------
# 6. Checking if a key exists
# ---------------------------------------------------------------
print("\n6. Checking keys")
print("Harry" in student_scores)  # True
print("Neville" in student_scores)  # False

# ---------------------------------------------------------------
# 7. Nesting
# ---------------------------------------------------------------
# Dictionaries can hold lists and other dictionaries.
print("\n7. Nesting")

# A list inside a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg"],
}
print("Second French city:", travel_log["France"][1])

# A dictionary inside a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total_visits": 5},
}
print("Germany visits:", travel_log["Germany"]["total_visits"])

# A list of dictionaries (very common when working with data)
travel_list = [
    {"country": "France", "visits": 12},
    {"country": "Germany", "visits": 5},
]
for entry in travel_list:
    print(entry["country"], entry["visits"])

# ---------------------------------------------------------------
# 8. Practical example: grading students
# ---------------------------------------------------------------
print("\n8. Grading example")
student_grades = {}
for name, score in student_scores.items():
    if score > 90:
        student_grades[name] = "Outstanding"
    elif score > 80:
        student_grades[name] = "Exceeds Expectations"
    elif score > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"
print(student_grades)

# ---------------------------------------------------------------
# 9. Handy extras
# ---------------------------------------------------------------
print("\n9. Extras")
print("Number of items:", len(student_scores))

defaults = {"theme": "dark", "volume": 5}
overrides = {"volume": 8, "language": "en"}
defaults.update(overrides)  # merges; overrides win on duplicate keys
print("Merged:", defaults)

# Dictionary comprehension: build a dict in one line
squares = {n: n**2 for n in range(1, 6)}
print("Squares:", squares)

# ---------------------------------------------------------------
# 10. Your turn! (try these)
# ---------------------------------------------------------------
# a) Make a dictionary of 3 friends and their favourite colours, then print one.
# b) Loop through it and print "<name> likes <colour>".
# c) Add a new friend, then delete another.
# d) Find the highest score in student_scores using a loop.
# e) Count how many times each letter appears in a word, using a dictionary.
