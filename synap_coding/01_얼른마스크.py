# 얼른 마스크씨 회사 전기 자동차의 행복한 일련번호
# 해당 문제의 핵심은 행복한 수가 되기 위한 조건이 무엇인가? 에 대한 부분이다.
# 행복한 수 = 자기 자리수 전체를 각각 분해하여 제곱했을 때 1이 나올 때까지 '반복' 하는 것이다.
# 즉, 조심해야할 부분이 1의 자리숫자가 나오더라도, 최초의 값이 나와서 영원히 반복되지 않는 한 계속 연산이 필요하다.
# 따라서 성능적인 면이 중요하더라도 이 부분을 해결할 수 있는 조건적 장치가 일단 필요하며
# 연산을 진행함에 따라 자기 자신이 나오진 않지만, 다른 값이 계속해서 나오는 경우의 조건도 해결이 필요하다(3은 계속 반복됨, 9는 최종적으로 4로 계속 귀결됨)
#

def practice_recursive(value, number_sheet, first_value):
    if number_sheet[value][0] == 1 and number_sheet[value][1]:
        return 1
    elif number_sheet[value][0] < 10 and number_sheet[value][0] != 0 and not number_sheet[value][1]:
        return number_sheet[value][0]
    else:
        target_string = str(value)
        total_number = 0
        for char in target_string:
            target_number = int(char)
            target_number *= target_number
            total_number += target_number
        if total_number > 9:
            total_number = practice_recursive(total_number, number_sheet, first_value)
        if total_number <= 9 and total_number != first_value and number_sheet[total_number] == 0:
            total_number = practice_recursive(total_number, number_sheet, first_value)
        return total_number


def happy_recursive(value, number_sheet, first_value):
    if number_sheet[value][0] != 0:
        return
    value_string = str(value)
    total_number = 0
    for char in value_string:
        target_number = int(char)
        target_number *= target_number
        total_number += target_number

    try:
        if total_number > 9:
            total_number = practice_recursive(total_number, number_sheet, first_value)
        if total_number <= 9 and total_number != first_value:
            total_number = practice_recursive(total_number, number_sheet, first_value)
    except RecursionError:
        number_sheet[value] = [first_value, False]
    else:
        if total_number == 1:
            number_sheet[value] = [1, True]
        elif total_number == first_value:
            number_sheet[value] = [total_number, False]
        elif total_number != first_value and number_sheet[total_number][1].__eq__(False) and total_number != 0:
            number_sheet[value] = [total_number, False]


k = int(input())

happy_number_sheet = dict()
for i in range(1, 10000):
    happy_number_sheet[i] = [0, False]

happy_number_sheet[1] = [1, True]

total_happy_number = 0
happy_number_counter = 0

for i in range(1, k + 1):
    happy_recursive(i, happy_number_sheet, i)
    if happy_number_sheet[i][0] == 1 and happy_number_sheet[i][1]:
        total_happy_number += i
        happy_number_counter += 1

for i in range(1, k + 1):
    print(i, ":", happy_number_sheet[i])

print(total_happy_number)
print("count : ", happy_number_counter)
print(total_happy_number * happy_number_counter)
