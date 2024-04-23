# 합 성공다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	283529	180963	153025	64.070%
# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.

# 예제 입력 1 
# 3
# 예제 출력 1 
# 6
# 출처
# Contest > Algorithmic Engagements > PA 2006 0-1번

# 문제를 번역한 사람: baekjoon
# 알고리즘 분류
# 수학
# 구현

# 기존버전 
n = int(input())
ret = 0
for i in range(1, n + 1):
  ret += i
print(ret)

# 개선버전 
# sum 과 range 의 조합 개꿀! ㄴ
print(sum(range(1, int(input()) + 1)))