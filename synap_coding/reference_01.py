import math

my_range = 9999
happy_num = []
for i in range(1, my_range + 1):
    temp_num_list = []
    temp = i
    while True:
        if temp == 1:
            happy_num.append(i)
            break
        if temp in temp_num_list:
            break
        temp_num_list.append(temp)
        if math.floor(temp / 1000) > 0:
            a = math.floor(temp / 1000)
            b = math.floor((temp % 1000) / 100)
            c = math.floor((temp % 1000) % 100 / 10)
            d = math.floor((temp % 1000) % 100 % 10)
            temp = a ** 2 + b ** 2 + c ** 2 + d
        elif math.floor(temp/100) > 0:
            a = math.floor(temp/100)
            b = math.floor((temp % 100) / 10)
            c = (temp % 100) % 10
            temp = a ** 2 + b ** 2 + c ** 2
        elif math.floor(temp/10) > 0:
            a = math.floor(temp / 10)
            b = (temp % 10)
            temp = a ** 2 + b ** 2
        else:
            temp = temp ** 2
# print(happy_num)
print(len(happy_num))
print(sum(happy_num))
print(sum(happy_num) * len(happy_num))