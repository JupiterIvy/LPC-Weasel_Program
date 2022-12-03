import random

phrase = input().upper()
generation = ""
count = 0

characters = [32, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

for i in range(len(phrase)):
    generation += (chr(random.choice(characters)))

darwin = generation

while darwin != phrase:
    count += 1
    if darwin != generation:
        for i in range(len(generation)):
            if abs(ord(generation[i]) - ord(phrase[i])) < abs(ord(darwin[i]) - ord(phrase[i])):
                darwin = darwin[:i] + generation[i] + darwin[i + 1:]
    generation = ""
    for i in range(len(phrase)):
        generation += (chr(random.choice(characters)))
    print(darwin, "Generation:", count)