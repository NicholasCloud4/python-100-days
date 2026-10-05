# Debugging in Python
# Each section has a buggy function, an explanation of the technique used to
# find the bug, and the fixed version.

# ---------- 1. Describe the problem: read the error ----------
# Python's traceback tells you the error type, the file, and the line.
# Uncomment the next line, run it, and read the message from the bottom up.
# print(int("hello"))  # ValueError: invalid literal for int() with base 10


# ---------- 2. Off-by-one error: "play computer" ----------
# Goal: print the numbers 1 to 5.
def count_to_five_buggy():
    for i in range(1, 5):  # BUG: range stops BEFORE the end value
        print(i, end=" ")
    print()


def count_to_five_fixed():
    for i in range(1, 6):
        print(i, end=" ")
    print()


print("Buggy:")
count_to_five_buggy()  # 1 2 3 4  (missing 5)
print("Fixed:")
count_to_five_fixed()

print("-" * 40)


# ---------- 3. Print debugging ----------
# Goal: find the largest number in a list.
def find_max_buggy(numbers):
    biggest = 0  # BUG: breaks if every number is negative
    for n in numbers:
        # Uncomment to watch what is happening on every loop:
        # print(f"n={n}, biggest={biggest}")
        if n > biggest:
            biggest = n
    return biggest


def find_max_fixed(numbers):
    biggest = numbers[0]  # start from a real value in the list
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest


data = [-5, -2, -9]
print(f"Buggy max: {find_max_buggy(data)}")  # 0, wrong!
print(f"Fixed max: {find_max_fixed(data)}")  # -2

print("-" * 40)


# ---------- 4. Assignment vs comparison, and wrong indentation ----------
# Goal: return "FizzBuzz" style output for 1-15.
def fizzbuzz_buggy(limit):
    results = []
    for number in range(1, limit + 1):
        if number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        elif number % 3 == 0 and number % 5 == 0:  # BUG: never reached
            results.append("FizzBuzz")
        else:
            results.append(number)
    return results


def fizzbuzz_fixed(limit):
    results = []
    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 == 0:  # most specific check first
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else:
            results.append(number)
    return results


print(f"Buggy 15: {fizzbuzz_buggy(15)[-1]}")  # Fizz
print(f"Fixed 15: {fizzbuzz_fixed(15)[-1]}")  # FizzBuzz

print("-" * 40)


# ---------- 5. Mutable default argument ----------
# Goal: each call should start with a fresh shopping list.
def add_item_buggy(item, basket=[]):  # BUG: the list is created only once
    basket.append(item)
    return basket


def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []  # a new list on every call
    basket.append(item)
    return basket


print(f"Buggy: {add_item_buggy('apple')}")
print(f"Buggy: {add_item_buggy('bread')}")  # ['apple', 'bread'] - leaked!
print(f"Fixed: {add_item_fixed('apple')}")
print(f"Fixed: {add_item_fixed('bread')}")  # ['bread']

print("-" * 40)


# ---------- 6. Handling errors with try / except ----------
# Some bugs come from user input you can't control.
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Debug: cannot divide by zero")
        return None


print(safe_divide(10, 2))
print(safe_divide(10, 0))

print("-" * 40)


# ---------- 7. Using assert to catch bugs early ----------
def average(numbers):
    assert len(numbers) > 0, "average() needs at least one number"
    return sum(numbers) / len(numbers)


print(average([2, 4, 6]))
# print(average([]))  # AssertionError with a helpful message

print("-" * 40)


# ---------- 8. The built-in debugger: breakpoint() ----------
# Uncomment the breakpoint() line and run the file. Execution pauses there
# and you get a (Pdb) prompt. Useful commands:
#   n          run the next line
#   s          step into a function call
#   c          continue until the next breakpoint
#   p name     print a variable (e.g. p total)
#   l          list the code around the current line
#   q          quit the debugger
def total_price(prices, tax_rate):
    total = 0
    for price in prices:
        total += price
        # breakpoint()
    return total * (1 + tax_rate)


print(f"Total: {total_price([10, 20, 30], 0.1):.2f}")  # 66.00

# In VS Code you can also click left of a line number to set a red
# breakpoint, then press F5 (Run and Debug) and use the Variables panel
# to inspect values while stepping with F10 (over) and F11 (into).
