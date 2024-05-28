# 특정 구간 내의 모든 피보나치 수의 합
# 특정 값(12345678999 ~ 99987654321) 사이의 피보나치 수를 더한 값이 얼마인가?
# 동적 프로그래밍 방식으로 기록하고, 계속해서 데이터를 쌓아가는 구조로 진행해야 한다.

min_limit, max_limit = map(int, input().split())
result = list()

a = 0
b = 1

while a <= max_limit:
    if a >= min_limit:
        result.append(a)
    a, b = b, a + b

print(result)
print(sum(result))