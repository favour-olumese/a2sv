class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        result = []
        for num in nums:
            if num in nums_dict:
                pass
            else:
                nums_dict[num] = nums.count(num)
        
        for key, value in nums_dict.items():
            if value > len(nums)/3:
                result.append(key)


        return result