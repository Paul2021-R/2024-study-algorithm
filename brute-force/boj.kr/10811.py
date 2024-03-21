import sys
N, M = map(int, sys.stdin.readline().split())
# actions = dict()
basket = list(x + 1 for x in range(N))

# 처음에 방법 : 2회전
# for i in range(M):
#     actions[i] = list(map(int, sys.stdin.readline().split()))
# for key in actions:
#     target = basket[actions[key][0] - 1:actions[key][1]]
#     target.reverse()
#     basket[actions[key][0] - 1:actions[key][1]] = target

# 두번째 방법 : 1회전, 압축 오브 압축, reversed 메소드를 호출하는 식으로 수정
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    start -= 1
    basket[start:end] = list(reversed(basket[start:end]))
print(*basket, sep='/') # * 언패킹 연산자로, 바로 출력하게 만드는 구조
