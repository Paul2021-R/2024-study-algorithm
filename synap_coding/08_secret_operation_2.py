# 암호 산술 2. COFFEE + COFFEE + COFFEE = ???
# 특정 단어 3개를 더하는 구조를 가진다고 할 때,
# words.txt 7 글자로 된 영어 단어들로 풀이가 된다고 할 때
# 그 중 78번째 단어를 찾고, 대문자로 제출할 것
# 조건
# 숫자 -> 영어 랑 매칭이 되어야 함.
# 숫자화 시키기 위해선 나온 숫자 + 영어 10자로 제한이 되어야 할까?  왜냐면 그렇지 않은 경우,
# 나머지 영어 알파벳에서 숫자를 지목해 내야함
# 따라서 말이 안됨, 그렇다면 10자로 제한을 걸어야하나?

coffee = "COFFEE"
result = dict()

with open('words.txt', 'r', encoding='utf8') as file:
    for line in file:
        arr = sorted(list(set(coffee + line)))
        if '\n' in arr:
            arr.remove('\n')
        if len(arr) == 10:
            result[line.replace("\n", "")] = list(arr)

        arr.clear()
    file.close()

for i, line in enumerate(result):
    # print(i, ":",  line, result[line])
    numbers = dict()
    for k, key in enumerate(result[line]):
        numbers[key] = k
    if numbers['C'] != 0 and numbers[line[0]] != 0:
        n_coffee = ""
        n_words = ""
        for key in coffee:
            n_coffee += str(numbers[key])
        for key in line:
            n_words += str(numbers[key])
        if int(n_coffee) * 3 == int(n_words):
            print(n_coffee, ":", n_words)
