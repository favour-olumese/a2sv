class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        temp = 0
        for i in range(len(nums) - 1, - 1, -1):
            if i != 0:
                temp = i
            if temp and nums[i] == 0:
                nums.append(nums.pop(i))
        return nums