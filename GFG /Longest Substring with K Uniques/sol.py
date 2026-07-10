def longestKSubstr(self, s, k):
    n = len(s)          # Length of the string
    left = 0            # Left pointer of the sliding window
    freq = {}           # Dictionary to store frequency of characters in current window
    res = -1            # Stores maximum length found, -1 if no valid substring exists

    # Expand the window by moving the right pointer
    for right in range(n):

        # Add current character into the window
        freq[s[right]] = freq.get(s[right], 0) + 1

        # --------------------------------------------------
        # If window has MORE than k distinct characters,
        # shrink it from the left until it has at most k.
        # --------------------------------------------------
        while len(freq) > k:

            # Remove the leftmost character from the window
            freq[s[left]] -= 1

            # If its frequency becomes 0,
            # completely remove it from dictionary
            if freq[s[left]] == 0:
                del freq[s[left]]

            # Move left pointer forward
            left += 1

        # --------------------------------------------------
        # If window has EXACTLY k distinct characters,
        # it is a valid answer.
        # --------------------------------------------------
        if len(freq) == k:

            # Update maximum length
            res = max(res, right - left + 1)

    # Return longest valid substring length
    return res
