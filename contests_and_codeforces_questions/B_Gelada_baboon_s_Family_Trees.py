# class UnionFind:
#     def __init__(self, size):
#         self.parent = {i: i for i in range(1, size + 1)}
 
#     def find(self, x):
#         return self.parent[x]
 
#     def union(self, x, y):
#         parentX = self.find(x)
#         parentY = self.find(y)
#         if parentX != parentY:
#             for node in self.parent:
#                 if self.parent[node] == parentX:
#                     self.parent[node] = parentY

#     def connected(self, x, y):
#         return self.find(x) == self.find(y)

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        # self.parent = {i: i for i in range(1, size + 1)}

    def find(self, city):
        # print(city)
        if city == self.parent[city]:
            return city
        self.parent[city] = self.find(self.parent[city])
        return self.parent[city]

    def union(self, city1, city2):
        root1 = self.find(city1)
        root2 = self.find(city2)
        if root1 != root2:
            self.parent[root2] = root1

    def connected(self, member1, member2):
        return self.find(member1) == self.find(member2)

fam_num = int(input())
fam = list(map(int, input().split()))
family = UnionFind(fam_num)

for i in range(1, fam_num + 1):
    # print(i, fam[i - 1])
    family.union(i, fam[i - 1])

fam_tree = set(family.parent[1:])
# print(family.parent)
print(len(fam_tree))
# Similar to this https://leetcode.com/problems/number-of-provinces/submissions/1379205538/