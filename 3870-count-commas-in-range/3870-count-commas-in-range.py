class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        start = 1000
        commas = 1

        while start <= n:
            end = n
            count += (end - start + 1) * commas
            start *= 1000
            commas += 1

        return count
         
             