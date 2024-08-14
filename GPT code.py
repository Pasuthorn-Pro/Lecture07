# Survey results (each list represents a participant's choices)
survey_results = [
    ["Python", "JavaScript", "C++"],      # Participant 1
    ["Python", "JavaScript", "C#"],       # Participant 2
    ["Python", "Java"],                   # Participant 3
    ["Python", "C++", "JavaScript"],      # Participant 4
    ["Python", "JavaScript", "C++", "Java"], # Participant 5
]

# Task 1: Identify the languages that were chosen by all participants.
all_languages = set(survey_results[0])
for choices in survey_results[1:]:
    all_languages.intersection_update(choices)

# Task 2: Find the languages that were only chosen by a single participant.
language_counts = {}
for choices in survey_results:
    for language in choices:
        language_counts[language] = language_counts.get(language, 0) + 1

unique_languages = {language for language, count in language_counts.items() if count == 1}

# Task 3: Determine the number of unique languages mentioned in the survey.
total_unique_languages = len(language_counts)

# Task 4: List the languages that were chosen by exactly two participants.
languages_chosen_by_two = {language for language, count in language_counts.items() if count == 2}

# Task 5: Find participants who have the exact same set of favorite languages.
identical_participants = []
for i in range(len(survey_results)):
    for j in range(i + 1, len(survey_results)):
        if set(survey_results[i]) == set(survey_results[j]):
            identical_participants.append((i + 1, j + 1))

# Output the results
print(f"Languages chosen by all participants: {all_languages}")
print(f"Languages chosen by only one participant: {unique_languages}")
print(f"Number of unique languages: {total_unique_languages}")
print(f"Languages chosen by exactly two participants: {languages_chosen_by_two}")
print(f"Participants with identical choices: {identical_participants}")
