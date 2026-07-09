class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeroCount = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans