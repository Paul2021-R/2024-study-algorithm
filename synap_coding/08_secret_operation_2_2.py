# 암호 산술 2. COFFEE + COFFEE + COFFEE = ???
# 특정 단어 3개를 더하는 구조를 가진다고 할 때,
# words.txt 7 글자로 된 영어 단어들로 풀이가 된다고 할 때
# 그 중 78번째 단어를 찾고, 대문자로 제출할 것
# 조건
# 숫자 -> 영어 랑 매칭이 되어야 함.
# 숫자화 시키기 위해선 나온 숫자 + 영어 10자로 제한이 되어야 할까?  왜냐면 그렇지 않은 경우, <- 이거 아님, 없어도 됨
# 나머지 영어 알파벳에서 숫자를 지목해 내야함
# 따라서 말이 안됨, 그렇다면 10자로 제한을 걸어야하나?
import itertools

coffee = "COFFEE"
keyword_all_numbers = dict()

with open('words.txt', 'r', encoding='utf8') as file:
    for line in file:
        arr = sorted(list(set(coffee + line)))
        if '\n' in arr:
            arr.remove('\n')
        if len(arr) != 11:
            keyword_all_numbers[line.replace("\n", "")] = list(arr)
    file.close()

min_number = 4
possibility_list = dict()

for i in range(min_number, 11):
    combi_list = []
    for combi in itertools.permutations(range(0, 10), i):
        combined_number = ''.join(map(str, combi))
        combi_list.append(combined_number)
    possibility_list[i] = combi_list


for key in keyword_all_numbers:
    # target_length = len(keyword_all_numbers[key])
    target_length = len(keyword_all_numbers[key])
    # print(target_length)
    target = possibility_list[target_length]
    for numbers in target:
        print(numbers)
    # target.clear()
