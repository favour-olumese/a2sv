damage_cap = list(map(int, input().split()))
nums = list(map(int, input().split()))

bilbo_side = 0
bilbo_oppo = 0
for i in range(0, 3):
    bilbo_side += (damage_cap[i] * nums[i])

for i in range(3, 5):
    bilbo_oppo += (damage_cap[i] * nums[i])

if bilbo_side > bilbo_oppo:
    print('WIN')
elif bilbo_side < bilbo_oppo:
    print('LOSE')
else:
    print('DRAW')