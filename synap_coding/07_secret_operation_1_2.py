# 암호 산술 1. SYNAP + SOFT = WANTS + YOU
# 각 알파벳은 하나의 숫자를 나타냄.
# SEND + MORE = MONEY -> 이걸 푸는 원리를 활용해
# SYNAP + SOFT = WANTS + YOU 를 구해보자
# 위 암호 산술의 가능한 모든 답의 좌변 숫자를 더한 값을 제출할것

# 로직
# 10 자의 영어단어
# 그 중, S, W, Y 는 0이 아님
# 그 외의 나머지 경우를 만들고
# 각 문자열 위치에 맞춰 숫자를 조합(사전형)
# 숫자랑 만들어진 숫자배열 -> 문자열 조합 만들기(숫자) -> 계산해보기 -> 맞으면? -> 결과 배열에 넣기

import itertools

# 문자 리스트
sy = "SYNAP"
so = "SOFT"
wa = "WANTS"
yo = "YOU"
n_sy = ""
n_so = ""
n_wa = ""
n_yo = ""

letters = set(x for x in sy + so + wa + yo)

arr = sorted(list(letters))

result = list()

for combi in itertools.permutations(arr, 10):
    combined_number = ''.join(map(str, combi))
    if (combined_number[0] != 'S' and combined_number[0] != 'W' and combined_number[0] != 'Y'):
        arr_dict = dict({char: i for i, char in enumerate(combined_number)})
        # print(arr_dict)

        for key in sy:
            n_sy += str(arr_dict[key])
        for key in so:
            n_so += str(arr_dict[key])
        for key in wa:
            n_wa += str(arr_dict[key])
        for key in yo:
            n_yo += str(arr_dict[key])

        # 숫자 해독이 가능한 케이스
        if int(n_sy) + int(n_so) == int(n_wa) + int(n_yo):
            result.append(dict(arr_dict))

        # 초기화
        arr_dict.clear()
        n_sy = ""
        n_so = ""
        n_wa = ""
        n_yo = ""
        # print(n_sy, n_so, n_wa, n_yo)

print(result)

total_value = 0
for interpreted_number in result:
    for key in sy:
        n_sy += str(interpreted_number[key])
    for key in so:
        n_so += str(interpreted_number[key])

    total_value += int(n_sy) + int(n_so)

    n_sy = ""
    n_so = ""

print(total_value)

