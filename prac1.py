""" Write a program that accepts a student's marks in five subjects and calculates 
the total, average, and grade using conditional statements (if-elif-else). 
Grade criteria: 
≥ 75: Distinction 
60–74: First Class 
50–59: Second Class 
35–49: Pass 
< 35: Fail """

def calculate_grade(average):
    if average >= 75:
        return "Distinction"
    elif 60 <= average <= 74:
        return "First Class"
    elif 50 <= average <= 59:
        return "Second Class"
    elif 35 <= average <= 49:
        return "Pass"
    else:
        return "Fail"

# Input marks for five subjects
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = []

print("Enter marks for each subject (out of 100):")
for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100")
        except ValueError:
            print("Please enter a valid number")

# Calculate total and average
total = sum(marks)
average = total / len(subjects)

# Get grade
grade = calculate_grade(average)

# Display results
print("\nResults:")
print("-" * 40)
for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark}")
print("-" * 40)
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")