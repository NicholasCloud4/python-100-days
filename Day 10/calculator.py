def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Error: cannot divide by zero"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number?: "))
    keep_going = True

    while keep_going:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        while operation not in operations:
            operation = input("Invalid operation. Pick one of + - * /: ")

        num2 = float(input("What's the next number?: "))
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        choice = input(
            f"Type 'y' to continue with {result}, 'n' to start a new calculation, or 'q' to quit: "
        ).lower()
        if choice == "y" and not isinstance(result, str):
            num1 = result
        elif choice == "n" or choice == "y":
            print("\n" * 20)
            calculator()
            return
        else:
            keep_going = False


calculator()
