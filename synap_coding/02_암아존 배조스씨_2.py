# 암아존 배조스씨를 위한 계좌이체 한글 음성 안내
# 백조원까지 단위별로 한글 읽기 출력이 이루어짐
# 천 백 십 일 조
# 천 백 십 일 억
# 천 백 십 일 만
# 천 백 십 일
# 어절 별 클래스 구성
# 어절 조건 -> 모든 값의 단위가 0이 아닐 때
# 기초 클래스(천단위) -> 모든 단위가 1글자

import sys

def count_word_first(number_part):
    result = 0
    for i, digit in enumerate(number_part):
        # print("요소 : ", i, digit)
        if i == 0:
            if digit != 0:
                result += 1
        if i != 0 and digit != 0:
            if digit == 1:
                result += 1
            else:
                result += 2
    return result

def count_word_second(number_part):
    result = 0
    for i, digit in enumerate(number_part):
        if i == 0 and digit != 0:
            result += 1
        if i != 0 and digit != 0:
            result += 2
    if result != 0:
        result += 1
    return result

def count_word_final(number_part, unit):
    result = 0
    if unit == 0:
        result += count_word_first(number_part)
    else:
        result += count_word_second(number_part)
    return result

def count_words(value, word_devision):
    result = 0
    value.reverse()
    part = []
    unit = 0
    for i, word in enumerate(value):
        temp = 0
        part.append(word)
        if i == 3:
            temp = count_word_first(part)
            part.clear()
            unit += 1
        elif i == 5 or i == 11 or i == 14:
            temp = count_word_second(part)
            part.clear()
            unit += 1
        elif i + 1 == len(value):
            temp = count_word_final(part, unit)
            part.clear()
        # if temp != 0 and unit != 0:
        #     word_devision += 1
        #     result += temp

        if temp != 0:
            word_devision += 1
            result += temp
            # print(word_devision, " : ", temp)
    result += 1
    value.reverse()
    print("값 :", value)
    print("어간: ", word_devision, "개")
    print("글자 개수: ", result, "개")
    return result * word_devision

k = int(input())
line = []
for i in range(k):
    line.append(sys.stdin.readline())

total_result = 0

for i in range(k):
    arr = []
    word_devision = 0
    for char in line[i].split(","):
        if "원" in char:
            char = char.replace("원\n", "")
        for number in char:
            arr.append(int(number))
    # print(arr)
    total_result += count_words(arr, word_devision)

print(total_result)
