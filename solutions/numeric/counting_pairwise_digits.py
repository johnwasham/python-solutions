'''
You are tasked with writing a function that takes a positive integer, n, as input and returns the number of times a digit appears immediately next to an identical digit in the number. In other words, your function should count how many times two equal digits appear consecutively when reading the number from left to right.

For example, if n = 113224, there are two instances where a digit is immediately followed by the same digit: 11 and 22. Therefore, the output should be 2. For n = 444, the output should be 2, as there are two places where a digit is immediately followed by the same digit (44 and another 44).

Keep in mind that n will be a positive integer ranging from 1 to 10^8, inclusive.

Note: You are not permitted to convert the number into a string or any other iterable structure for this task. You should work directly with the number.
'''

def solution(n):
    count = 0
    start = True
    last_digit = 0
    while n > 0:
        digit = n % 10
        if start:
            start = False
        else:
            if digit == last_digit:
                count += 1
        last_digit = digit
        n = n // 10

    return count


print(solution(22544400))
# 4
