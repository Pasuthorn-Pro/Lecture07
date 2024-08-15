survey_results = [
    ["Python", "Javascript", "C++"],
    ["Python", "Javascript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "Javascript"],
    ["Python", "Javascript", "C++", "Java"]
]

language_counts = {}
for choices in survey_results:
    for language in choices:
        language_counts[language] = language_counts.get(language, 0) + 1

print(language_counts)
unique_languages = {language for language, count in language_counts.items() if count == 1}
print(f"Languages chosen by only one participant: {unique_languages}")