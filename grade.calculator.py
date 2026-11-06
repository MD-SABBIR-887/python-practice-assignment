# Practice Problem 2: Student Grade Calculator

name = input("Enter your name: ")
math = float(input("Enter your Math marks: "))
english = float(input("Enter your English marks: "))
python = float(input("Enter your Python marks: "))
avarage_mark = (math + english + python) / 3

if (
    math < 0 or math > 100 or
    english < 0 or english > 100 or
    python < 0 or python > 100
):
    print("Invalid marks! Marks must be between 0 and 100.")
else:
    if avarage_mark >= 80:
        grade = "A+"
    elif avarage_mark >= 70:
        grade = "A"
    elif avarage_mark >= 60:
        grade = "A-"
    elif avarage_mark >= 50:
        grade = "B"
    elif avarage_mark >= 40:
        grade = "C"
    else:    
        grade = "F"
        
    print (f"hello {name}")
    print (f"your average mark is {avarage_mark:.2f}")
    print (f"your grade is {grade}")