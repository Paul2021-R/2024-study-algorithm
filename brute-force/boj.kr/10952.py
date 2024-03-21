import sys

arr = []
while (True):
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    arr.append(a + b)

print('\n'.join(str(x) for x in arr if x % 2 == 0))