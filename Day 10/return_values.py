def format_name(first_name, last_name):
    """Format a full name with the first and last name capitalized.

    Parameters:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.

    Returns:
        str: The formatted full name or an error message if either name is missing.
    """

    if not first_name or not last_name:
        return "You need to add a first and last name."

    return f"{first_name.title()} {last_name.title()}"

print(format_name(input("First name: "), input("Last name: ")))