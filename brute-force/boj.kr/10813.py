import sys
N, M = map(int, sys.stdin.readline().split())
basket = list(x + 1 for x in range(N))
actions = dict()
for i in range(M):
    actions[i] = list(map(int, sys.stdin.readline().split()))
for key in actions:
    var1 = basket[actions[key][0] - 1]
    var2 = basket[actions[key][1] - 1]
    basket[actions[key][0] - 1] = var2
    basket[actions[key][1] - 1] = var1
print(' '.join(str(x) for x in basket))
