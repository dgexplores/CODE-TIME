from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        j = 1
        m = [nums[0]]

        while j < len(nums):
            if nums[j] != nums[i]:
                m.append(nums[j])
                i = j

            j += 1

        for k in range(len(m)):
            nums[k] = m[k]

        return len(m)