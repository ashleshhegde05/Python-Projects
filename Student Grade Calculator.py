# Student Grade Calculator

def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

marks = []

subjects = int(input("Enter number of subjects: "))

for i in range(subjects):
    mark = float(input(f"Enter marks for Subject {i+1}: "))
    marks.append(mark)

average = calculate_average(marks)

print("\nAverage Marks =", round(average,2))
print("Grade =", assign_grade(average))