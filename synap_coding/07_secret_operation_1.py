# 암호 산술 1. SYNAP + SOFT = WANTS + YOU
# 각 알파벳은 하나의 숫자를 나타냄.
# SEND + MORE = MONEY -> 이걸 푸는 원리를 활용해
# SYNAP + SOFT = WANTS + YOU 를 구해보자
# 위 암호 산술의 가능한 모든 답의 좌변 숫자를 더한 값을 제출할것

import itertools

# 문자 리스트
letters = 'SYNAPSOFTWU'
# 문자에 대한 인덱스를 저장할 딕셔너리
letter_index = {letter: idx for idx, letter in enumerate(letters)}

# 결과를 저장할 리스트
results = []

# 각 조합에 대해 검증
for perm in itertools.permutations(letter_index.keys(), len(letters)):
    print("perm:", perm)
    perm_numbers = ''.join(map(str, perm))
    print(perm_numbers)

    # S, W는 0이 될 수 없음
    if perm[letter_index['S']] == 0 or perm[letter_index['W']] == 0:
        continue

    # 문자에 숫자 매핑
    mapping = {letter: digit for letter, digit in zip(letters, perm)}

    # 숫자로 변환
    SYNAP = mapping['S'] * 10000 + mapping['Y'] * 1000 + mapping['N'] * 100 + mapping['A'] * 10 + mapping['P']
    SOFT = mapping['S'] * 1000 + mapping['O'] * 100 + mapping['F'] * 10 + mapping['T']
    WANTS = mapping['W'] * 10000 + mapping['A'] * 1000 + mapping['N'] * 100 + mapping['T'] * 10 + mapping['S']
    YOU = mapping['Y'] * 100 + mapping['O'] * 10 + mapping['U']

    # 방정식 검증
    if SYNAP + SOFT == WANTS + YOU:
        results.append((SYNAP, SOFT, WANTS, YOU))

# 결과 출력
if results:
    total_sum = sum(SYNAP + SOFT for SYNAP, SOFT, _, _ in results)
    print(f"가능한 모든 답의 좌변 숫자를 더한 값: {total_sum}")
else:
    print("가능한 답이 없습니다.")
