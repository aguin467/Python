# Storing user input into a list using the input function
user_grades = [int(n) for n in input('Enter numbers: ').split()]
maximum = max(user_grades)
minimum = min(user_grades)

while True:  # Using while loop to always evaluate true to print maximum and minimum values stored in user_grades
    print("Maximum Value,", maximum)
    print("Minimum Value,", minimum)
    break


# Finding the average of user_grades by using the sum function divided by the function length of user_grades
average = sum(user_grades) / len(user_grades)

print("The average is:", average)
