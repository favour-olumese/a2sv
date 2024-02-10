class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                right[:0] = [pivot]
            else:
                right.append(num)

        return left + right