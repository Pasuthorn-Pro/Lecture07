attendance_week  = [
    ["Alice", "Bob", "Chalie", "David"],
    ["Alice", "Chalie", "David"],
    ["Alice", "Bob", "David"],
    ["Alice", "David", "Eve"],
    ["Bob", "Chalie", "David"]
]

attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

present_every_day = set.intersection(*attendance_sets)
print("Present every day: ", present_every_day)

all_student = set.union(*attendance_sets)
absent_at_least_one_day = all_student - present_every_day
print("Absent at least one day: ", absent_at_least_one_day)

first_day_present = attendance_sets[0]
last_day_present = attendance_sets[-1]
first_but_not_last = list(first_day_present - last_day_present)
print("Present on first day but absent on last day: ", first_but_not_last)

unique_students_count = len(all_student)
print("Total unique students: ", unique_students_count)