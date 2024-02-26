if __name__ == '__main__':
    score_list = []
    name_list = []
    slg = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        score_list.append(score)
        name_list.append(name)
        
    score_set = set(score_list)
    mini = min(score_set)
    score_set.remove(mini)
    next_mini = min(score_set)
    
    for i in range(len(score_list)):
        if score_list[i] == next_mini:
            slg.append(name_list[i])
            
    slg.sort()
    
    for name in slg:
        print(name)