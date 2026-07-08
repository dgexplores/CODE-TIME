def longestKSubstr(self, s, k):
        n = len(s)
        left = 0
        freq = {}
        res = -1

        for right in range(n):
            freq[s[right]] = freq.get(s[right], 0) + 1

            # shrink window if > k unique
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            # if exactly k unique, check length
            if len(freq) == k:
                res = max(res, right - left + 1)

        return res
