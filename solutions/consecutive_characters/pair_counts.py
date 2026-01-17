"""
In this task, you need to write a Python function that finds repeating two-character patterns in a string. The function should identify when the same pair of characters appear next to each other in the string and count how many times each pair repeats consecutively.

The function should return a new string that lists each pair followed by the number of times it repeats consecutively. For example, let's break down the input string "aaabbabbababacab":

Divide the string into pairs:

"aa"
"ab"
"ba"
"bb"
"ab"
"ab"
"ac"
"ab"
Note the consecutive pairs:

"ab" appears twice consecutively in the middle.
Therefore, the output string will be: "aa1ab1ba1bb1ab2ac1ab1".

Similarly, for the input string "aaababbababaca", the output should be "aa1ab2ba3ca1".

Key points to remember:

The input string always has an even number of characters.
The string contains only lowercase letters.
The string length can be up to 500 characters.
Focus on finding consecutive repetitions of the same two-character patterns.
"""


def solution(s):
    result = []

    group_str = None
    count = 0
    n = len(s)

    for i in range(0, n, 2):
        pair = s[i:i + 2]

        if pair == group_str:
            count += 1
        else:
            if group_str is not None:
                result.extend([group_str, str(count)])
            group_str = pair
            count = 1

    if group_str is not None:
        result.extend([group_str, str(count)])

    return ''.join(result)


assert solution("aaabbabbababacab") == "aa1ab1ba1bb1ab2ac1ab1"
assert solution("aaababbababaca") == "aa1ab2ba3ca1"