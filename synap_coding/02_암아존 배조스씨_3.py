# 암아존 배조스씨를 위한 계좌이체 한글 음성 안내
# 최적화 버전

import sys


def count_word(number_part, unit):
    result = 0
    addtional_result = 0
    for i, digit in enumerate(number_part):
        # 첫자리 숫자에 대한 조건들
        # 일반적인 숫자인 경우
        if i == 0 and digit != 0 and digit != 1:
            result += 1
        elif i == 0 and digit == 1: # 최초숫자이면서 1인 경우, 일십~ 일조 까지 최초 일이 오는 경우를 검증
            checker = False
            for other_index in range(1, len(number_part)):
                if int(number_part[other_index]) != 0:
                    checker = True # 일단위보다 높은 같은 발음 자리에서 숫자가 존재해 일이란 발음이 들어가야 하는경우
                    break
            if checker:
                result += 1
            else:
                addtional_result += 1 # 같은 단위 기준, 다른 숫자가 없어서 단위수만 붙으면 된다. 혹은 일만 붙어야 한다.

        # 다른 자리숫자들의 값에 대한 카운트
        if i != 0 and digit != 0:
            if digit == 1:
                result += 1
            else:
                result += 2

    # 최종적으로 결과가 있고, 단위숫자가 만 이상이면, 단위숫자를 붙여준다.
    if unit != 0 and result != 0:
        addtional_result = 1
    return result + addtional_result


def count_words(value):
    value.reverse()
    part = []
    result = 0
    number_unit = 0 # 단위 수
    word_division = 0 # 어간의 숫자
    temp = 0
    for word_index, word in enumerate(value):
        part.append(word)
        if len(part) == 4 or (word_index + 1 == len(value)):
            temp = count_word(part, number_unit)
            number_unit += 1
            part.clear()
        if temp != 0:
            word_division += 1
            result += temp
            temp = 0

    result += 1
    return result * word_division


k = int(input())
line = []
for i in range(k):
    line.append(sys.stdin.readline())

total_result = 0

for i in range(k):
    arr = []
    for char in line[i].split(","):
        if "원" in char:
            char = char.replace("원\n", "")
        for number in char:
            arr.append(int(number))
    total_result += count_words(arr)

print("어간 x 글자수 : ", total_result)
