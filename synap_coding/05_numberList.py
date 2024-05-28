# 숫자 목록을 이용해 만든 두 자연수 합의 최솟값

import itertools

arr = list(map(int, input().split(", ")))
print(arr)
combi = dict()
maximum_comb = len(arr)
for i in range(maximum_comb // 2 , maximum_comb // 2 + 1):
    # print(i, "/", maximum_comb - i)
    for combination in itertools.permutations(arr, i):
        combined_number = ''.join(map(str, combination))
        if combined_number in combi.keys():
            pass
        if combined_number[0] != '0':
            # print(combined_number)
            new_arr = list(arr)
            for char in combined_number:
                new_arr.remove(int(char))
            # print("new_array:", new_arr)
            combi[int(combined_number)] = set()
            for opposite_combination in itertools.permutations(new_arr, maximum_comb - i):
                if opposite_combination[0] != '0':
                    combined_opposite_number = ''.join(map(str, opposite_combination))
                # print("상대 숫자:", combined_opposite_number)
                    if combined_opposite_number[0] != '0':
                        combi[int(combined_number)].add(int(combined_opposite_number))
                        print(combined_opposite_number)
                # elif combined_opposite_number[0] = '0' and int(combined_opposite_number) == 0:
                #     combi[int(combined_number)].clear()
            # sorted(combi[int(combined_number)])
print("keys:", combi.keys())
result = set()
for i in combi.keys():
    # print(i, ":", min(combi[i]))
    if len(combi[i]) == 0:
        # result.add(-1)
        # break
        pass
    else:
        result.add(i + min(combi[i]))
    # result.add(i + min(combi[i]))
# key = min(combi.keys())
# value = min(combi[key])
# print(key, value )
#
# print(key + value)
print(result)
print(min(result))