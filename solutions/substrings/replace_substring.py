"""
Imagine you are working on a new feature for a text processing application. The feature requires you to provide users with the option to replace all occurrences of a certain substring in the entered text with a new substring.

You are tasked with writing a function, replace_substring(text: str, old: str, new: str) -> str, that does the following:

Accepts as input text (a string of length n, where 1 ≤ n ≤ 500, which includes only lowercase alphabets and spaces), old (a string of length k, where 1 ≤ k ≤ n, which includes only lowercase alphabets), and new (a string of length m, where 1 ≤ m ≤ 500, which includes only lowercase alphabets).

Replaces every occurrence of the string old in text with the string new.

Returns the updated text string with all replaced substrings.

Please ensure that the case of the letters remains consistent during the process, meaning an uppercase letter should be replaced with an uppercase letter, and a lowercase letter should be replaced with a lowercase one.

For instance, your function might be called as follows:

Python
Copy to clipboard
replace_substring("hello world", "world", "friend")
In this case, the output would be: "hello friend"
This is because there is one occurrence of the substring 'world' in the string. This occurrence is replaced by 'friend', resulting in the return value "hello friend".
"""

def replace_substring(text, old, new):
    return text.replace(old, new)


assert replace_substring("hello world", "world", "friend") == "hello friend"