n = int(input())

for i in range(n):
    n, m , k = list(map(int, input().split()))
    alice = input()
    alice.sort()
    bob = input()
    bob.sort()

    if alice[0] > bob[0]:
        alice, bob = bob, alice

        
