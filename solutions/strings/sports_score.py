"""
You are given a string s of length n, with n ranging from 1 to 500 inclusive. This string represents the complex and jumbled record of a sports game. It combines player names and scores but lacks a uniform structure. The player names consist of words made up of lowercase English alphabets (a-z), while the scores are integers ranging from 1 to 100 inclusive.

Your mission involves writing a Python function solution(). This function should parse the given string, isolate the integers representing player scores, and return the sum of these scores.
"""


def solution(s):
    result = []

    num = ""

    for c in s:
        if not c.isnumeric():
            if num:
                result.append(int(num))
                num = ""
        elif c.isnumeric():
            num += c

    if num:
        result.append(int(num))

    return sum(result)

    assert solution(
        "joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe", ) == 18
