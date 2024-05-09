# 최댓값 성공
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	323598	148915	123077	45.425%
# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#
# 예를 들어, 서로 다른 9개의 자연수
#
# 3, 29, 38, 12, 57, 74, 40, 85, 61
#
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
#
# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
#
# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
#
# 예제 입력 1
# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61
# 예제 출력 1
# 85
# 8
# 출처
# Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2007 > 초등부 1번
#
# 데이터를 추가한 사람: sait2000

# 최초 버전
# import sys
#
# numbers = list()
# i = 1
# while i < 10:
#     a = int(sys.stdin.readline())
#     numbers.append(a)
#     i += 1
# maxValue = max(numbers)
# print(maxValue)
# print(numbers.index(maxValue) + 1)

# 개선버전
# 조금이라도 성능 향상이 있고, 순회를 1회로 만들 수 있는 버전
import sys

maxValue = 0
maxIndex = 0
for i in range(9):
    a = int(sys.stdin.readline())
    if a > maxValue:
        maxValue = a
        maxIndex = i

print(maxValue)
print(maxIndex + 1)