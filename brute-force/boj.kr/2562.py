import sys

numbers = list()
i = 1
while i < 10:
    a = int(sys.stdin.readline())
    numbers.append(a)
    i += 1
maxValue = max(numbers)
print(maxValue)
print(numbers.index(maxValue) + 1)
