#This is a GPA to Grade converter. (The scale is according to HKU's GPA scale)

course = input("Enter the course name: ").upper()

percent = float(input("Enter the percent: "))

if percent >= 80 and percent <= 84:
    grade = float("3.7")
    print(f"The grade is A- Congrat!")

elif percent >= 85 and percent <= 89:
    grade = float("4.0")
    print(f"The grade is A Congrat!")

elif percent >= 90 and percent <= 100:
    grade = float("4.3")
    print(f"The grade is A+ Congrat!")

elif percent >= 76 and percent <= 79:
    grade = float("3.3")
    print(f"The grade is B+ Very Good")

elif percent >= 73 and percent <= 75:
    grade = float("3")
    print(f"The grade is B Average Good")

elif percent >= 70 and percent <= 72:
    grade = float("2.7")
    print(f"The grade is B- Borderline Good")

elif percent >= 66 and percent <= 69:
    grade = float("2.3")
    print(f"The grade is C+ Add Oil")

elif percent >= 63 and percent <= 65:
    grade = float("2.0")
    print(f"The grade is C Add Oil")

elif percent >= 60 and percent <= 62:
    grade = float("1.7")
    print(f"The grade is C- Add Oil")

elif percent >= 55 and percent <= 59:
    grade = float("1.3")
    print(f"The grade is in D+ pass")

elif percent >= 50 and percent <= 54:
    grade = float("1.0")
    print(f"The grade is D just pass")

elif percent >= 0 and percent <= 49:
    grade = float("0")
    print(f"Failure. Quit U la on9 jai")

else:
    print(f"Plz enter the correct percentage")

print(f"The GPA of {course} is {grade}")
