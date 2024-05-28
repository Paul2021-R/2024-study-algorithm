# 암호 산술 2. COFFEE + COFFEE + COFFEE = ???
# 특정 단어 3개를 더하는 구조를 가진다고 할 때,
# words.txt 7 글자로 된 영어 단어들로 풀이가 된다고 할 때
# 그 중 78번째 단어를 찾고, 대문자로 제출할 것
# 조건
# COFFEE 라는 글자는 정해져 있음
# 따라서 해당 글자에 맞춰 패턴을 지정을 하고
# 해당 패턴에 따라 나온 COFFEE* 3 을 한 값이 존재 할 때, 해당 하는 값들의 패턴을 검색하는 방식으로 접근하면 안될까?
# COFFEE 102233 => 306699 => 이 패턴에 충족하는 경우를 모두 고르면 된다.
import itertools

coffee = "COFFEE"
keyword_all_numbers = dict()
mixed_number_list = {}

with open('words.txt', 'r', encoding='utf8') as file:
    for line in file:
        keyword_all_numbers[line.strip()] = set()
    file.close()
# print(keyword_all_numbers.keys())

for mixed in itertools.permutations(range(0, 10), 4):
    mixed_number = ''.join(map(str, mixed))
    if mixed_number[0] != '0':
        c = mixed_number[0]
        o = mixed_number[1]
        f = mixed_number[2]
        e = mixed_number[3]
        mixed_number_list[mixed_number] = [c+o+f+f+e+e, str(int(c+o+f+f+e+e) * 3)]

origin_number_dict = {str(x): -1 for x in range(0, 10)}
result = []
for key in mixed_number_list:
    # print(key, ":", mixed_number_list[key])
    pattern = mixed_number_list[key][1]
    # print(mixed_number_list[key][0], ":", pattern)
    cofe = ['C', 'O', 'F', 'E']
    n_cofe = list(map(int, key))
    for target in keyword_all_numbers.keys():
        copy_dict = origin_number_dict.copy()
        checker = True
        for char_num, char in zip(pattern, target):
            if copy_dict[char_num] == -1:
                copy_dict[char_num] = char
            elif copy_dict[char_num] != -1:
                if copy_dict[char_num] == char:
                    pass
                else:
                    checker = False
                    break
            for i, number in enumerate(n_cofe):
                if (copy_dict[str(n_cofe[i])] == cofe[i]) or (copy_dict[str(n_cofe[i])] == -1):
                    copy_dict[str(n_cofe[i])] = cofe[i]
                else:
                    checker = False
                    break
        if checker:
            result.append([key, mixed_number_list[key][0], pattern, target])
            break
print(result)
