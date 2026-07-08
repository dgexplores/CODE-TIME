class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ml = float('inf')
        cnt = 0

        for r in range(len(nums)):
            cnt += nums[r]

            while cnt >= target:
                ml = min(ml, r - l + 1)
                cnt -= nums[l]
                l += 1

        if ml == float('inf'):
            return 0

        return ml