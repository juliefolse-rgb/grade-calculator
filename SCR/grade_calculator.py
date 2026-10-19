def validate_input(value):
    # check whether the value is valid
    if value < 0:
        print("Error: please enter a number that is 0 or greater.")
        return False
    return True


def get_points_possible():
    # keep asking until the user enters a valid value
    while True:
        points_possible = float(input("Enter the total points possible: "))
        if validate_input(points_possible):
            if points_possible == 0:
                print("Error: points possible cannot be 0.")
            else:
                return points_possible


def get_points_earned():
    # keep asking until the user enters a valid value
    while True:
        points_earned = float(input("Enter the points earned: "))
        if validate_input(points_earned):
            return points_earned


def calculate_grade(points_earned, points_possible):
    # calculate the percentage and round to two decimal places
    return round(points_earned / points_possible * 100, 2)


def get_letter_grade(percentage):
    # use an if/elif/else chain to determine the letter grade
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def display_grade(percentage, letter_grade):
    # print the results in the required format
    print(f"Your grade: {percentage:.2f}%")
    print(f"Your letter grade: {letter_grade}")


# main program: call the functions in order
points_possible = get_points_possible()
points_earned = get_points_earned()
percentage = calculate_grade(points_earned, points_possible)
letter_grade = get_letter_grade(percentage)
display_grade(percentage, letter_grade)