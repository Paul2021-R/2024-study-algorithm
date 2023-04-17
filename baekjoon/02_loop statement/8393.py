# https://www.acmicpc.net/problem/8393
n = int(input())
ret = 0
for i in range(1, n + 1):
  ret += i
print(ret)

# 최적화, 가우스 방정식 적용 예시
n = int(input())
print (n *(n + 1)//2)