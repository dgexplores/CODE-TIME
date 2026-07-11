
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        ans = 0

        for right in range(len(s)):
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1

            max_freq = max(freq.values())
            window_length = right - left + 1
            replacements = window_length - max_freq

            while replacements > k:
                freq[s[left]] -= 1
                left += 1

                max_freq = max(freq.values())
                window_length = right - left + 1
                replacements = window_length - max_freq

            ans = max(ans, right - left + 1)

        return ans