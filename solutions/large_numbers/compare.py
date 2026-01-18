"""
For this task, you are given two non-negative integers, num1 and num2. However, these are not just ordinary numbers; they are so large that they should be represented as strings instead of normal integers. Each can be up to 100 digits long.

Your mission is to write a Python function that compares these two "string-numbers" without converting the entire strings into integers. Your function should determine whether num1 is greater than, less than, or equal to num2.

Your function can only use comparison operators (such as >, <, or ==) on strings. So “1” < “2” is allowed, but 1 < 2 is not. The task requires that you manually compare the two strings from the most significant digit to the least significant. You should implement your own logic to compare two string numbers.

The function should return the following results:

If num1 is greater than num2, your function should return 1.
If num2 is greater than num1, your function should return -1.
If num1 and num2 are equal, your function should return 0.
"""


def solution(num1, num2):
    len1 = len(num1)
    len2 = len(num2)

    if len1 > len2:
        return 1
    elif len2 > len1:
        return -1

    for i in range(len1 - 1, -1, -1):
        a = num1[i]
        b = num2[i]

        if a == b:
            continue
        elif a > b:
            return 1
        else:
            return -1

    return 0


assert solution("1234", "1235") == -1
assert solution("12345", "9999") == 1
assert solution("12345", "12345") == 0
