class Solution:
    def shuffle(self, nums: list[int], n: int) -> List[int]:
        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])


        return result