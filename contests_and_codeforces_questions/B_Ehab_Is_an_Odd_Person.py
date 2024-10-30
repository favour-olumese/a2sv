def find_lexicographically_smallest(nums):
    n = len(nums)

    # Separate elements into even and odd lists
    even, odd = [], []
    for i, num in enumerate(nums):
        if num % 2 == 0:
            even.append((num, i))  # Store element and index for evens
        else:
            odd.append(num)

    # Append odd elements first (lexicographically smaller)
    result = odd

    # Handle even elements
    if even:
        # Sort even elements by value (ascending order)
        even.sort()

        # Check if swaps are necessary for even elements
        # (if first element is larger than the last remaining odd element)
        if result and result[-1] > even[0][0]:
            # Find the first index in evens that's larger than the last odd
            for i, (num, _) in enumerate(even):
                if num > result[-1]:
                    # Swap the last odd element with the current even element
                    result[-1], even[i][0] = even[i][0], result[-1]
                    break

        # Append remaining even elements (already sorted)
        result.extend([num for num, _ in even])

    return result

# Example usage
n = int(input())
nums = list(map(int, input().split()))
result = find_lexicographically_smallest(nums)
print(*result)