# https://www.acmicpc.net/problem/11021
import sys

for i in range(0, int(sys.stdin.readline().rstrip())):
    print("Case #" + str(i + 1) + ": " +
          str(sum(map(int, sys.stdin.readline().split()))))
