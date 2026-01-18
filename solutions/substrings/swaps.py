"""
Humans often make mistakes when they are typing quickly. In some cases, they may press two keys simultaneously, resulting in swapped characters in the text. Your task is to craft a Python function that helps identify such typos. Specifically, you are asked to construct a function called spot_swaps(source: str, target: str) -> List[Tuple[int, str, str]] that behaves as follows:

Given two strings, source and target, of the same length n (1 ≤ n ≤ 500), inclusive, both comprise only lowercase English letters. The function should return a list of tuples. Each tuple should contain three elements: the zero-based index of the swap in the source string, the character (a string of length 1) at that index in source, and the character that swapped places with the source character in target.

In other words, go over both strings simultaneously and, for each character from source and target at position i, find situations when source[i] != target[i] and source[i+1] = target[i] and source[i] = target[i+1]. This implies that the characters at positions i and i+1 in the source string swapped places in the target string.

Note:

Characters can be swapped at most once.
The swapped character pairs should be returned in a list in the order they were found (from the string start to end).
Don't check for swaps at the last position of a string, since there is no character with which to swap.
"""


def spot_swaps(source: str, target: str) -> list[tuple[int, str, str]]:
    result = []

    n = len(source)
    i = 0

    while i < n - 2:
        if source[i] != target[i] and source[i] == target[i + 1] and source[i + 1] == target[i]:
            result.append((i, source[i], target[i]))
            i += 2
        else:
            i += 1

    return result


assert spot_swaps("hello", "hlelo") == [(1, 'e', 'l')]
