class Solution:
    def longestArithmetic(self, nums):
        n = len(nums)

        if n <= 2:
            return n

        L = [1] * n
        R = [1] * n

        L[0] = 1
        L[1] = 2
        for i in range(2, n):
            d1 = nums[i] - nums[i - 1]
            d2 = nums[i - 1] - nums[i - 2]
            if d1 == d2:
                L[i] = L[i - 1] + 1
            else:
                L[i] = 2

        R[n - 1] = 1
        R[n - 2] = 2
        for i in range(n - 3, -1, -1):
            d1 = nums[i + 1] - nums[i]
            d2 = nums[i + 2] - nums[i + 1]
            if d1 == d2:
                R[i] = R[i + 1] + 1
            else:
                R[i] = 2

        ans = 2

        for i in range(n):
            if i > 0:
                ans = max(ans, L[i - 1] + 1)

            if i + 1 < n:
                ans = max(ans, R[i + 1] + 1)

            if i > 0 and i + 1 < n:
                gap = nums[i + 1] - nums[i - 1]

                if gap % 2 == 0:
                    d = gap // 2

                    leftLen = 1
                    if i >= 2 and nums[i - 1] - nums[i - 2] == d:
                        leftLen = L[i - 1]

                    rightLen = 1
                    if i + 2 < n and nums[i + 2] - nums[i + 1] == d:
                        rightLen = R[i + 1]

                    ans = max(ans, leftLen + 1 + rightLen)

        return min(ans, n)