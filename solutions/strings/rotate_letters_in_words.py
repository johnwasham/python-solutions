"""
You are given a string of n characters, with n varying from 1 to 1000, inclusive. Your task is to write a Python function that takes this string as input, applies the following operations, and finally returns the resulting string.

Split the given string into individual words, using a space as the separator.
Convert each word into a list of its constituent characters, and shift each list once to the right (with the last element moving to the first position).
After the rotations, reassemble each word from its list of characters.
Join all the words into a single string, separating adjacent words with a single space.
Return this final string as the function's output.
The constraints for the problem are as follows:

The input string will neither start nor end with a space, nor will it have multiple consecutive spaces.
Each word will contain only alphabets and digits, and its length will range from 1 to 10.
The words are case-sensitive; for example, 'word' and 'Word' are considered distinct.
Your program should output a single string with the words rotated by their lengths while preserving their original order.

As an illustration, consider the input string "abc 123 def". Applying the stated operations results in the output "cab 312 fde".
"""


def solution(s):
    result = []

    tokens = s.split()

    for token in tokens:
        letters = list(token)
        n = len(letters)
        for i in range(n - 1, 0, -1):
            nxt = (i + 1) % n
            temp = letters[nxt]
            letters[nxt] = letters[i]
            letters[i] = temp

        new_word = ''.join(letters)
        result.append(new_word)

    return ' '.join(result)


assert solution("abc 123 def") == "cab 312 fde"
