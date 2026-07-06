class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        count = 0
        n = len(arr)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                sumn = arr[i] + arr[left] + arr[right]

                if sumn < sum:
                    # All triplets from left to right are valid
                    count += (right - left)
                    left += 1
                else:
                    right -= 1

        return count