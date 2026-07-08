# Longest Substring with K Unique Characters

## Problem
Given a string `s` consisting only of lowercase alphabets and an integer `k`, find the length of the longest substring that contains exactly `k` distinct characters.

If no such substring exists, return `-1`.

## Input
- `s`: a string of lowercase letters.
- `k`: an integer representing the required number of distinct characters.

## Output
- An integer representing the length of the longest substring with exactly `k` distinct characters.
- Return `-1` if no valid substring exists.

## Examples

Example 1:
```
Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
```

Example 2:
```
Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.
```

Example 3:
```
Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.
```

## Notes
- The substring must contain exactly `k` distinct characters, not fewer.
- The substring should be contiguous.
