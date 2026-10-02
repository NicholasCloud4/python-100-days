student_scores = [85, 92, 78, 90, 88]

highest_score = max(student_scores)
print(f"The highest score is: {highest_score}")


# can also do 
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"The highest score is: {max_score}")