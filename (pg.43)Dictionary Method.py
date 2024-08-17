student = {"Name" : "Alice", "Age" : 25, "Major" : "Computer Science"}

print(student.keys())

print(student.values())

print(student.items())

print(student.get("Name"))
print(student.get("Grade", "Not Found"))

major = student.pop("Major")
print(major)
print(student)

last_item = student.popitem()
print(last_item)
print(student)

student.clear()
print(student)