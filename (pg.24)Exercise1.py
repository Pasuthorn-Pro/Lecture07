survey_results = [
    ["Python", "Javascript", "C++"],
    ["Python", "Javascript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "Javascript"],
    ["Python", "Javascript", "C++", "Java"]
]

choices_sets = [set(languages) for languages in survey_results]

common_languages = set.intersection(*choices_sets)
print(f"Languages chosen by all participants: {common_languages}")

language_counts = {}
for choices in survey_results:
    for language in choices:
        language_counts[language] = language_counts.get(language, 0) + 1

unique_languages = {language for language, count in language_counts.items() if count == 1}
print(f"Languages chosen by only one participant: {unique_languages}")

total_unique_languages = len(language_counts)
print(f"Number of unique languages: {total_unique_languages}")

languages_chosen_by_two = {language for language, count in language_counts.items() if count == 2}
print(f"Languages chosen by exactly two participants: {languages_chosen_by_two}")

identical_participants = []
for i in range(len(survey_results)):
    for j in range(i + 1, len(survey_results)):
        if set(survey_results[i]) == set(survey_results[j]):
            identical_participants.append((i + 1, j + 1))
print(f"Participants with identical choices: {identical_participants}")
