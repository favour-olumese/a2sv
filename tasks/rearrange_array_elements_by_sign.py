class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        rearranged = []

        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
        
        for i in range(len(positive)):
            rearranged.append(positive[i])
            rearranged.append(negative[i])

        return rearranged