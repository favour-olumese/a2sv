class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set = set(nums)

        if len(nums) > len(nums_set):
            return True
        return False