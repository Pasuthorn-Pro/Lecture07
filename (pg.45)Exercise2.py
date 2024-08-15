performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Chalie": [60, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85]
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66]
    }
}

#Calculate average
average_scores = {}
for department, employees in performance_data.items():
    average_scores[department] = {}
    for employee, scores in employees.items():
        average = sum(scores) / len(scores)
        average_scores[department][employee] = average

print(f"{average_scores}")

#Identify top performer in each department on average scores
identify_top_performer = {}
for department, employees in average_scores.items():
    top_performer = max(employees, key=employees.get)
    identify_top_performer[department] = (top_performer, employees[top_performer])
    
print(f"{identify_top_performer}")