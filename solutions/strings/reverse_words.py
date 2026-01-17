"""
Consider a string filled with words. Your task is to write a Python function that accepts such a string. It then takes each of those words, reverses their character order, and, finally, stitches them all together to form a new string with reversed words.

Here's what you need to keep in mind:

The input string will contain between 1 and 100 words.
Each word is a sequence of characters separated by white space.
A word is composed of characters ranging from a to z, A to Z, 0 to 9, or even an underscore _.
The given string will not start or end with a space - double spaces will not appear either.
After reversing the words, your program should return a single string with the words preserving their original order.
"""


def reverse_words(s):
    result = [t[::-1] for t in s.split()]

    return ' '.join(result)


assert reverse_words("Hello fellow kids a_123") == "olleH wollef sdik 321_a"