"""
Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def longest_substring_without_repeating_chr(s: str) -> int:
    tmp = []

    for idx, i in enumerate(s):
        tmp.append([i])
        j = idx + 1
        while j < len(s):
            if s[j] not in tmp[-1]:
                tmp[-1].append(s[j])
                j += 1
            else:
                break

    result = max(len(item) for item in tmp)

    return result

def fast_longest_substring_without_repeating_chr(s: str) -> int:
    seen = set()
    max_len = 0
    left = 0

    for right, letter in enumerate(s):

        while letter in seen:
            seen.remove(s[left])
            left += 1

        seen.add(letter)
        max_len = max(max_len, right - left + 1)

    return max_len

s = "abcabcbb"
longest_substring_without_repeating_chr(s)
fast_longest_substring_without_repeating_chr(s)

s = "bbbbb"
longest_substring_without_repeating_chr(s)
#
s = "pkwwkesw"
longest_substring_without_repeating_chr(s)
fast_longest_substring_without_repeating_chr(s)
