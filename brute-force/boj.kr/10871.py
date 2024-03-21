import sys
N, X = map(int, sys.stdin.readline().split())
numbers = [x for x in map(int, sys.stdin.readline().split())]
answer = ""
for i in numbers:
    if i < X:
        answer += str(i) + ' '

print(answer)