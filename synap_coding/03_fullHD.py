# 1920*1080 화면에서 지정된 직사각형 넓이를 다 더하는 문제
# 이 문제의 핵심은 두 점이 주어지고, 그 점을 기준 직사각형을 만들었을 때, 그 점위들의 종합을 계산하는 것이다.
# 여기서 핵심은 얼마나 데이터를 남길 것이며, 어떤 데이터는 버릴 것인가에 대한 정보이다.
# 핵심은 세로줄을 기준으로 제공이 들어오면,
# 가로 줄에서 어디까지를 사용범위로 둘지 기재하는 방식
# 사전 형태가 가지는 특성을 잘 활용한다면 충분히 해결이 가능한 문제다.

# 1920 의 가로 길이 만큼의 사전형
# 그 지목된 세로 위치 좌표를 리스트로 가짐
# 1920개의 사전 자료 기준으로 돌면서, 지목된 세로 좌표를 전체 개수를 구하고 더하면 됨
# 내부 자료는 집합형을 사용하면 됨


maximum_range = 1921

def total_sum(display_dots):
    result = 0
    for index in range(len(display_dots)):
        result += len(display_dots[index])
    return result


display = {x: set() for x in range(maximum_range)}

# with open('sample_box.txt', 'r', encoding='utf-8') as file:
with open('box.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # print(line.strip())
        x_1, y_1, x_2, y_2 = map(int, line.strip().split())
        # print(x_1, y_1, "/", x_2, y_2)
        for x in range(x_1, x_2):
            # print(x)
            for y in range(y_1, y_2):
                # print("coord", x, y)
                display[x].add(y)
    file.close()

    # for x in range(maximum_range):
    #     print(display[x])

    print(total_sum(display))
