# https://www.acmicpc.net/problem/25314

# 1차버전
n = int(input())
for _ in range(n//4):
    print("long ", end="")
print("int")

# 2차 개선 버전
print(int(input())//4 * 'long ' + 'int')
