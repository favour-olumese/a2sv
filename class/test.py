def arrayManipulation(n, queries):
    # Write your code here
    nums = [0 for x in range(n)]
    
    for query in queries:
        a, b, k = query
        
        # if a == b and b == n:
        #     a = b = n - 1
        # elif b >= n:
        #     b = n - 1

        for i in range(a - 1, b):
            print(i)
            nums[i] += k
        print(nums)
    
    return max(nums)

print(arrayManipulation(4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]]))
print(arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
