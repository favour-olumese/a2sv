class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        total = 0
        for operation in operations:
            if '+' in operation:
                total += 1
            elif '-' in operation:
                total -= 1

        return total