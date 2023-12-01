import re

with open("input02.txt", "r") as f:
    # with open("input.txt", "r") as f:
    data = f.readlines()

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

mapping = {k: v for k, v in zip(words, digits)}
mapping.update({d: d for d in digits})

keys = digits + words

numbers = []
for line in data:
    counts = []
    for key in keys:
        pos = line.find(key)
        if pos != -1:
            counts.append((key, pos))
    counts_sorted = sorted(counts, key=lambda item: item[1])
    numbers.append(int(mapping[counts_sorted[0][0]] + mapping[counts_sorted[-1][0]]))

print(numbers)
print("The sum is:", sum(numbers))
