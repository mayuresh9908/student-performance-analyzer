print("Student Performance Analyzer")
print("----------------------------")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

average = (maths + physics + chemistry) / 3

print("\nStudent:", name)
print("Average marks:", round(average, 2))
