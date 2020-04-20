name = input()

level = 1
bad_grades = 0
total_grade = 0
while level <= 12:
    if bad_grades == 2:
        print(f"{name} has been excluded at {level} grade")
        break
    grade = float(input())
    if grade < 4:
        bad_grades +=1
    else:
        total_grade += grade
        level +=1
if bad_grades <2:
    print(f"{name} graduated. Average grade: {total_grade /12 :.2f}")