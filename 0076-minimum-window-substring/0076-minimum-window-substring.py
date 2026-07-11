class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = {}
        window = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        have = 0
        required = len(need)

        min_len = float('inf')
        result = ""

        # RIGHT moves automatically →
        for right in range(len(s)):
            # right: 0 → 1 → 2 → 3 → 4 ...

            ch = s[right]

            # Add the RIGHT character
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            # When window is valid
            while have == required:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # Remove the LEFT character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                # LEFT moves manually →
                left += 1

        return result