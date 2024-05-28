# 스프레드 시트 컬럼의 영문명칭 계산
# 27진법 연산기 만들기
# 100,000,000 번째의 알파벳은?
# 26진수를 만들어내면 된다.
# 이때 핵심은 값의 시작점이 1인 경우로 이야기 하지만 0으로 시작해줘야하고,
# 그러다보니 들어오는 값, 나누느 뒤의 값에 1을 빼줘야 한다.
# 하지만 문제는 1을 빼주다가 0이 나오면, 실제 0이 나오는 경우와 혼선이 발생해서
# 이를 해결하고 진행해야 한다.
alpha = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
         5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
         10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
         15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
         20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

target = int(input('Enter a number: ')) - 1
result = ""
while target > 0:
    result += alpha[target % 26]
    target = target // 26
    if target == 1:
        result += alpha[0]
        break
    else:
        target -= 1

result = result[::-1]
print(result)
