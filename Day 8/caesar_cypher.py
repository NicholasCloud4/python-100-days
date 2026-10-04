alphabet = list("abcdefghijklmnopqrstuvwxyz")


def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1

    result = ""
    for char in text:
        if char in alphabet:
            new_position = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[new_position]
        else:
            result += char
    return result


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(f"The {direction}d text is: {caesar(text, shift, direction)}")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
 