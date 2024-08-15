student = {"Name" : "Alice", "Age" : 25, "Grade" : "A"}

student["Age"] = 26
student["Major"] = "Computer Science"
print(student)

del student["Grade"]
print(student)

removed_major = student.pop("Major")
print(removed_major)
print(student)