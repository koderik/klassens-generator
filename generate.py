import random
from unicodedata import name


def file_reader(filename):
    with open(filename) as adjective_file:
        content = []
        for row in adjective_file:
            content.append(row.strip())
    return content


def get_phrase(adjectives, nouns, name):
    adjectives_choice = random.sample(adjectives, k=3)
    noun_choice = random.choice(nouns)
    phrase = (
        name
        + " är I-21:s "
        + adjectives_choice[0]
        + ", "
        + adjectives_choice[1]
        + " och "
        + adjectives_choice[2]
        + " "
        + noun_choice
        + "!"
    )
    return phrase


adjectives = file_reader("adjectives.txt")
nouns = file_reader("nouns.txt")
names = file_reader("names.txt")

phrases = []

for name in names:
    phrases.append(get_phrase(adjectives, nouns, name))


with open("phrases.txt", "w") as phrase_file:
    for line in phrases:
        phrase_file.write(line + "\n")
