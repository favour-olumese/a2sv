if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr_set = set(arr)
    maxi = max(arr_set)
    arr_set.remove(maxi)
    
    next_maxi = max(arr_set)
    print(next_maxi)