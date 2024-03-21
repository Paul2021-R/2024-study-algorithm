import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
# print(scores)

M = max(scores)

scores = [x/M * 100 for x in scores]
# print(scores)
print(sum(scores)/N)