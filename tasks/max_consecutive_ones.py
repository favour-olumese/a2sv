class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        total = 0
        for num in nums:
            if num == 1:
                total += 1
            else:
                if maxi < total:
                    maxi = total
                total = 0

        if maxi < total:
            maxi = total

        return maxi