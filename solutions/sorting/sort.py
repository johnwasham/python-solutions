
nums = [45, 4, 5, 6, 13, 2, 6, 7, 9, 12, 55]

print(sorted(nums))
print(sorted(nums, reverse=True))

word_counts = {
    "food": 34,
    "water": 5,
    "fire": 10,
    "matches": 15
}

print(sorted(word_counts, key=lambda x: word_counts[x]))
print(sorted(word_counts, key=lambda x: word_counts[x], reverse=True))

tups = [
    (1414, "joe"),
    (1525, "sam"),
    (1414, "rocky"),
    (1414, "bluey"),
    (999, "joel"),
]

print(sorted(tups, key=lambda x: x[1])) # sort by name
print(sorted(tups, key=lambda x: x[0])) # sort by num
print(sorted(tups, key=lambda x: (x[0], x[1]))) # sort by num then name
print(sorted(tups, key=lambda x: (-x[0], x[1]))) # sort by num desc then name asc

