import heapq

tests = int(input())

for _ in range(tests):
    no = int(input())
    nums = list(map(int, input().split()))
    nums1 = [ele * -1 for ele in nums]

    if set(nums) == 1:
        print(nums[0] - 1)

    heap = []
    for i in range(no - 1):
        for j in range(i + 1, no):

            heapq.heappush(heap, nums[i:j + 1])

    print(heap)
    print(heapq.heappop(heap) - 1)


    # nums1 = [ele * -1 for ele in nums]
    # heapq.heapify(nums1)
    # print(nums1)
    # heap = []

    # for i in range(no - 1):
    #     # # print(heap1)
    #     # print(heap, 'bf', nums1[i])
    #     # heapq.heappushpop(heap, nums1[i])
    #     # print(heap, 'after')
    #     print(nums1[i: i + 2], 'nh')
    #     val = heapq.heappop(nums1[i: i + 2])
    #     print(val)
    #     heapq.heappush(heap, val)
    #     print(heap)
        
    # print(heapq.heappop(heap) - 1)
    # print('----------------')
    
