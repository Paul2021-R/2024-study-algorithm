n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    c = a + b
    number = i + 1
    str = "Case #"
    print(str, number, ": ", a, " + ", b, " = ", c, sep='')