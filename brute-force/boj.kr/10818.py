import sys

N = int(sys.stdin.readline())
# numbers = [x for x in map(int, sys.stdin.readline().split())]
numbers = list(map(int, sys.stdin.readline().split()))
print(str(min(numbers)) + ' ' + str(max(numbers)))
