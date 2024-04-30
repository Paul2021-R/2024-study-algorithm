# 시험 성적 성공
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	406053	221517	186176	54.829%
# 문제
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 시험 성적을 출력한다.

# 예제 입력 1 
# 100
# 예제 출력 1 
# A
# 출처
# 문제를 만든 사람: baekjoon
# 알고리즘 분류
# 구현

# 초기버전
import sys
a = int(sys.stdin.readline())
answer = ""

if 90 <= a:
    answer = "A"
elif 80 <= a <= 89:
    answer = "B"
elif 70 <= a <= 79:
    answer = "C"
elif 60 <= a <= 69:
    answer = "D"
else:
    answer = "F"
print(answer)


# 수정 버전 
import sys
a = int(sys.stdin.readline()) // 10
answer = { 0:"F", 1: "F", 2:"F", 3:"F", 4:"F", 5:"F", 6:"D", 7:"C", 8:"B", 9:"A", 10:"A"}
print(answer[a])

# 결론 : 둘이 차이 없는 속도를 내더라