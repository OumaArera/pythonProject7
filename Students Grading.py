student_scores = {
 "Harry": 81,
 "Ron": 78,
 "Hermione": 99,
 "Draco": 74,
 "Neville": 62,
}

student_grades ={}

for key in student_scores:
    if student_scores[key] <= 70:
        student_grades[key] = "Fail"
        print(student_grades)

    elif student_scores[key] <= 80:
        student_grades[key] = "Acceptable"

    elif student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"

    elif student_scores[key] <= 100:
        student_grades[key] = "Outstanding"

for key in student_grades:
    print(f"Score of {key} is {student_grades[key]}")


