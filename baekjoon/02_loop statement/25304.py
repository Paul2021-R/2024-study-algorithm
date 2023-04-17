# https://www.acmicpc.net/problem/25304

total = int(input())
cnt = int(input())
arr = []
for _ in range(cnt):
  key, val = map(int, input().split())
  pair= [key, val]
  arr.append(pair)

ret = sum(pair[0] * pair[1] for pair in arr)

print("Yes") if ret == total else print("No")

# 상당히 깎은 대표 예시 
import sys
input = sys.stdin.readline
total = int(input())
for i in range(int(input())):
    a,b = map(int,input().split())
    total -= a*b
print("Yes" if total == 0 else "No")