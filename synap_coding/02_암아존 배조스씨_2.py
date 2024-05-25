# 암아존 배조스씨를 위한 계좌이체 한글 음성 안내
# 백조원까지 단위별로 한글 읽기 출력이 이루어짐
# 천 백 십 일 조 (14)
# 천 백 십 일 억 (11)
# 천 백 십 일 만 (7)
# 천 백 십 일 (3)
# 핵심조건 !!!
# 만 단위 부터는 십단위 이상 이 있으면 일만 이라고 읽지만, 십단위가 없이, 1이 나오면 만원 으로 읽는다

import sys

def count_word(number_part, unit):
    result = 0
    addtional_result = 0
    for i, digit in enumerate(number_part):
        if i == 0 and digit != 0 and digit != 1:
            result += 1
        elif i == 0 and digit == 1:
            checker = False
            for k in range(1, len(number_part)):
                # print(number_part[k])
                if int(number_part[k]) != 0:
                    checker = True
                    break
            if checker:
                result += 1
            else:
                addtional_result += 1
        if i != 0 and digit != 0:
            if digit == 1:
                result += 1
            else:
                result += 2

    if unit != 0 and result != 0:
        addtional_result = 1
    return result + addtional_result

def count_words(value, word_devision):
    result = 0
    value.reverse()
    part = []
    unit = 0
    for i, word in enumerate(value):
        temp = 0
        part.append(word)
        if len(part) == 4:
            print(i, word, ":", part)
            temp = count_word(part, unit)
            unit += 1
            part.clear()
        elif i + 1 == len(value):
            print(i, word, ":", part)
            temp = count_word(part, unit)
            unit += 1
            part.clear()
        if temp != 0:
            print("unit", unit - 1,  "글자 수: ", temp)
            word_devision += 1
            result += temp

    result += 1
    print("어간:", word_devision, "개")
    print("글자 개수:", result, "개")
    print("곱한 값:", result * word_devision)
    print("===========================")
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
    total_result += count_words(arr, word_devision)

print("어간 x 글자수 : ", total_result)
