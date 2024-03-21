import sys

N = int(sys.stdin.readline())
numberList = [x for x in map(int, sys.stdin.readline().split())]
V = int(sys.stdin.readline())
numberDict = {V: 0}
for key in numberList:
    if key in numberDict:
        numberDict[key] += 1
    else:
        numberDict[key] = 1
print(numberDict[V])