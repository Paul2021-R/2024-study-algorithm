# 숫자 목록을 이용해 만든 두 자연수 합의 최솟값
# 구현의 핵심은 덧셈과 양 수를 나눈다는 점.
# 결국 숫자들의 배열을 받는다고 하면
# 최솟값을 만드는 것은 곱셈이 아니므로, 각 숫자가 제일 큰 단위부터 최소의 값으로 배정이 되어야 하고
# 0은 둘째 자리부터 넣을 수 가 있을 것이며,
# 전체 들어온 숫자의 자릿수를 절반 정도씩으로 나눴을 때, 비로소 최소 합산 값을 구할 수 있다!
# 전체 경우의 수를 다 세는 건 몇 자리 안될 때나 가능한 이야기다.
# 핵심 1 - 각 숫자의 앞자리는 무조건 최소 값으로 지정 미리해주기
# 핵심 2 - 전체 들어온 배열 길이 중, 자릿수를 감안 조합을 구성해냄
# 핵심 3 - 0 의 경우 가능한 앞에 배치 되는게 적절함

arr = list(map(int, input().split(", ")))
zero_arr = list()
print(arr)
numberA = ""
numberB = ""
while True:
    if 0 in arr:
        zero_arr.append(0)
        arr.remove(0)
    else:
        break

min_value = min(arr)
numberA += str(min_value)
arr.remove(min_value)

min_value = min(arr)
numberB += str(min_value)
arr.remove(min_value)

i = 0
while len(arr) != 0 :
    if i % 2 != 0:
        if 0 in zero_arr:
            zero_arr.remove(0)
            numberB += '0'
        else:
            min_value = min(arr)
            arr.remove(min_value)
            numberB += str(min_value)
    else :
        if 0 in zero_arr:
            zero_arr.remove(0)
            numberA += '0'
        else:
            min_value = min(arr)
            arr.remove(min_value)
            numberA += str(min_value)
    i += 1

print("A:", numberA)
print("B:", numberB)
print(int(numberA) + int(numberB))