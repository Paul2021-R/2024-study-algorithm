# 최소, 최대 성공
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	383276	172347	129889	43.872%
# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
#
# 예제 입력 1
# 5
# 20 10 35 30 7
# 예제 출력 1
# 7 35

# 상당히 느린 버전
# import sys
#
# N = int(sys.stdin.readline())
# numbers = [x for x in map(int, sys.stdin.readline().split())]
# numbers.sort()
# print(str(numbers[0]) +' ' + str(numbers[-1]))

# 중간 버전
# import sys
#
# N = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
# print(str(min(numbers)) + ' ' + str(max(numbers)))

# 개선 버전 2
# min, max의 경우 최적화 시킬 수 있는 경우를 다 처리하고 진행되므로,
# 그러한 최적화를 넣고 루프를 한 번 도는 것과 min, max를 개별로 처리하는 것이랑 비슷한 결과가 나온다.
import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
min_value = numbers[0]
max_value = numbers[0]
if len(numbers) == 1:
    pass
elif len(numbers) == 2:
    if numbers[0] > numbers[1]:
        min_value = numbers[1]
        max_value = numbers[0]
    else:
        min_value = numbers[0]
        max_value = numbers[1]
else:
    min_value = min(numbers)
    max_value = max(numbers)
print (str(min_value) + ' ' + str(max_value))
