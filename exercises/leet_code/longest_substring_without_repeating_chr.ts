/*
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
 */

function longetsSubstring(data: string):number {
    let seen = new Set<string>()
    let maxLength = 0
    let left = 0


    for (let right = 0; right < data.length; right++) {
        const letter = data[right]

        while(seen.has(data[right]!)) {
            seen.delete(data[left]!);
            left++
        }

        seen.add(letter!)
        maxLength = Math.max(maxLength, right - left + 1)
    }

    console.log(maxLength)

    return maxLength
}

const s = "pkwwkesw"
longetsSubstring(s)

const s1 = "abcabcbb"
longetsSubstring(s1)
