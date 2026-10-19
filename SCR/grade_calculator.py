# prompt the user for points possible and cast to a float
points_possible = float(input("Enter the total points possible: "))

# prompt the user for points earned and cast to a float
points_earned = float(input("Enter the points earned: "))

# use conditionals to handle incorrect input
if points_possible < 0 or points_earned < 0:
    print("Error: please enter numbers that are 0 or greater.")
elif points_possible == 0:
    print("Error: points possible cannot be 0.")
else:
    # calculate the grade and round to two decimal places
    grade = round(points_earned / points_possible * 100, 2)

    # print the grade in the required format
    print(f"Your grade: {grade:.2f}%")

    # use an if/elif/else chain to assign a letter grade
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"

    # print the letter grade in the required format
    print(f"Your letter grade: {letter}")