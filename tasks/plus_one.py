class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = map(str, digits)
        number = int(''.join(digits_str))
        number += 1
        return list(map(int, str(number)))