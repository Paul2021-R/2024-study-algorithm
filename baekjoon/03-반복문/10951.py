# A+B - 4 성공
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	396537	143032	119872	35.942%
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

# 예제 입력 1 
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2
# 예제 출력 1 
# 2
# 5
# 7
# 17
# 7
# 출처
# 문제를 만든 사람: baekjoon
# 빠진 조건을 찾은 사람: djm03178
# 비슷한 문제
# 1000번. A+B
# 1001번. A-B
# 1008번. A/B
# 2558번. A+B - 2
# 10950번. A+B - 3
# 10952번. A+B - 5
# 10953번. A+B - 6
# 10998번. A×B
# 11021번. A+B - 7
# 11022번. A+B - 8
# 15740번. A+B - 9
# 15792번. A/B - 2
# 알고리즘 분류
# 수학
# 구현
# 사칙연산

# 기존버전
import sys

while (True):
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break

# 개선버전
import sys

answer = ""
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        answer += str(a + b) + "\n"
    except:
        break
print(answer)