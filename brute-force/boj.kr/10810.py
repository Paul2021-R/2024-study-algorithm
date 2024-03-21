import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0] * N
countAction = dict()

for i in range(M):
    countAction[i] = list(map(int, sys.stdin.readline().split()))

for key in countAction:
    # print("key : ", key)
    for i in range(countAction[key][0],countAction[key][1] + 1):
        basket[i - 1] = countAction[key][2]
print(' '.join(str(x) for x in basket))
