# ------------challenge-1: grading program-----------------
print("------------------challenge-1----------------------")
student_scores = {
    "Gyamzo": 83,
    "Harry": 78,
    "Kane": 56,
    "Saka": 67,
    "Don": 98
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    # print(student)
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_scores)
print(student_grades)

# ------------challenge-2: dictionary in list-----------------
print("------------------challenge-2----------------------")
travel_log = [
    {
        "country": "Nepal",
        "cities": ["Pokhara", "Dharan", "Illam", "Kathmandu"],
        "visits":12
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Munchen", "Dortmund"],
        "visits":5
    },
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
print(f"you have visited {travel_log[0]['country']} {travel_log[0]['visits']} times")
print(f"you have been to {travel_log[0]['cities'][0]}")