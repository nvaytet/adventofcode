import re

with open("input01.txt", "r") as f:
    data = f.readlines()

numbers = []
for line in data:
    numbers_as_strings = re.findall(r"\d", line)
    # numbers_on_line = [int(number) for number in numbers_as_strings]
    if len(numbers_as_strings) > 1:
        numbers.append(int(numbers_as_strings[0] + numbers_as_strings[-1]))
    elif len(numbers_as_strings) > 0:
        numbers.append(int(numbers_as_strings[0] * 2))

print(numbers)
print("The sum is:", sum(numbers))
