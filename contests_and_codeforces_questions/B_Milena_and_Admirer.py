tests = int(input())
 
for _ in range(tests):
    no = int(input())
    nums = list(map(int, input().split()))
    
    if sorted(nums) == nums:
        print(0)
    else:
        length = no - 1
        count = 0
        while length > 0:
 
            if nums[length - 1] <= nums[length]:
                length -= 1
            else:
                count += 1
                temp = nums.pop(length - 1)
                temp1 = temp // 2
                nums.insert(length -1, temp - temp1)
                nums.insert(length - 1, temp1)
                length += 1
                
        print(count)