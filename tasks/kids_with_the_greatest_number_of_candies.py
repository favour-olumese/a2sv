class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        truth = []
        for i in range(len(candies)):
            candies_list = candies.copy()
            candies_list[i] += extraCandies
            if max(candies_list) == candies_list[i]:
                truth.append(True)
            else:
                truth.append(False)

        return truth      