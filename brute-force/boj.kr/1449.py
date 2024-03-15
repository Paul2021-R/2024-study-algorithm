N, L = map(int, input().split())
breakPoint = [int(x) for x in input().split()]
breakPoint.sort()


# print("N : ", N)
# print("L : ", L)
# print("breakPoint: ", breakPoint)

def f(a, b, c):
    print("min : ", a, "/ max : ", b, "/ total tapes : ", c)


minTape = breakPoint[0] - 0.5
maxTape = minTape + L
ans = 1
# f(minTape, maxTape, ans)

for i in range(N):
    if (minTape < breakPoint[i]) and (maxTape > breakPoint[i]):
        continue
    else:
        ans += 1
        minTape = breakPoint[i] - 0.5
        maxTape = minTape + L
    # f(minTape, maxTape, ans)

print(ans)


# 저자가 이야기 하는 방법
N, L = map(int, input().split())
cord = [False] * 1001
for i in map(int, input().split()):
    cord[i] = True

ans = 0
x = 0
while x < 1001:
    if cord[x]:
        ans += 1
        x += L
    else:
        x += 1

print(ans)