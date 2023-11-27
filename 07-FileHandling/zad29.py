def calculate_mean(grades):
    return sum(grades) / len(grades)

# Read grades from the file
with open("grades.txt", 'r') as file:
    # Read lines from the file
    lines = file.readlines()

    # Extract grades from the "Grades:" line and convert them to float
    grades_str = lines[1].split(':')[1].strip()
    grades = [float(grade) for grade in grades_str.split(',')]

    # Calculate the mean
    mean = calculate_mean(grades)

    # Display the result
    print(f"Arithmetic Mean: {mean}")