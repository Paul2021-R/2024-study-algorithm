# 암아존 배조스씨를 위한 계좌이체 한글 음성 안내
# 백조원까지 단위별로 한글 읽기 출력이 이루어짐
# 천 백 십 일 조
# 천 백 십 일 억
# 천 백 십 일 만
# 천 백 십 일
# 어절 별 클래스 구성
# 어절 조건 -> 모든 값의 단위가 0이 아닐 때
# 기초 클래스(천단위) -> 모든 단위가 1글자
class NumberUnit:
    def __init__(self, value, end):
        self.value = value
        self.numb_arr = {x: 0 for x in range(4, 1)}
        i = len(value)
        for char in value:
            self.numb_arr[i] = int(char)
            i -= 1


        if end:
            self.type = 1000 # 천단위
        else:
            self.type = 0 # 다른 숫자들
        if sum(self.numb_arr) == 0:
            self.type = -1 # 계산할 필요 없음
    def get_hangule_count(self):
        if self.type == -1:
            return 0
        total = 0
        print(self.numb_arr)
        return 0
        # if self.type == 1000:
        #     return 0
        # else:
        #     return 0

    def get_value(self):
        return self.value

import sys

line = []
for i in range(1):
    line.append(sys.stdin.readline())

어절 = 0
한글 = 0
for i in range(1):
    arr = []
    for char in line[i].split(","):
        # print(char)
        if "원" in char:
            char = char.replace("원\n", "")
            arr.append(NumberUnit(char, True))
        else:
            arr.append(NumberUnit(char, False))
    for element in arr:
        print(element.get_value(), " : ", element.get_hangule_count())
# print(line)