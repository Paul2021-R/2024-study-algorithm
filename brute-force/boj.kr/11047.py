n, k = map(int, input().split())
# print("n = ", n)
# print("k = ", k)

coins = [int(input()) for _ in range(n)]
coins.reverse()
# print(coins)
howManyCoins = 0
i = 0
# 구하는데 성공은 했지만 시간초과를 받앗다.
# while k > 0:
#     while i < n:
#         if coins[i] <= k:
#             howManyCoins += 1
#             k = k - coins[i]
#             if coins[i] > k:
#                 i += 1
#         else:
#             i += 1

# 시간초과를 피하기 위해선 한번에 계산 되어야 함
for coin in coins:
    if coin <= k: # 조건문으로 쓰지 않는 코인을 스킵하는 것은 속도가 큰 차이가 없다.
        howManyCoins += k // coin
        k %= coin
    else:
        continue

print(howManyCoins)