# Create a list of scores
scores = [55, 87, 67, 54, 77]
print (f"Scores = {scores}")
print()

# Define a function named calculate_average
def calculate_average(scores):
    # Assign total to an empty value 0
    total = 0
    # Use for loop to create your loop in order to sum the scores
    for score in scores:
        total += score
    # Calculate avergae and assign it to a variable named average
    average = float(total / len(scores))
    return(average)

average = calculate_average(scores)
print(f"Average score of scores is {average}")
print()

# Define a function get_grade(average) that takes an average score and returns a letter grade
# where A = 90–100, B = 75–89, C = 60–74, F = below 60

def get_grade(average):
    # Use conditional statement to assign letter grade to score
    if 90 <= average <= 100:
        return("Grade A")
    elif 75 <= average <= 89:
        return("Grade B")
    elif 60 <= average <= 74:
        return("Grade C")
    else:
        return("Grade F")

grade = get_grade(average)
print(f"Your grade is {grade}")
print()

# generate_report(name, scores)
# That takes a student name and a list of scores
# then prints the student's name, their average, and their letter grade in a readable format.

def generate_report(name, scores):
    average = calculate_average(scores)
    grade = get_grade(average)
    print(f"Student name:", name,
          "\n""Average:", average,"\n",grade)

generate_report("Bolu Ojo", [54, 90, 33, 47, 60])
print()
generate_report("Shade Kai", [65, 45, 70, 76, 88])