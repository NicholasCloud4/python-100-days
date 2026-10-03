def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()

    true_count = 0
    for letter in "true":
        true_count += combined.count(letter)

    love_count = 0
    for letter in "love":
        love_count += combined.count(letter)

    print(f"{true_count}{love_count}")


# Call your function with hard coded values
calculate_love_score("Kanye West", "Kim Kardashian")
