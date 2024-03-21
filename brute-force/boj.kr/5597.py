import sys

students = [False] * 31
# print(students)
students[0] = True
for i in range(28):
    student = int(sys.stdin.readline())
    students[student] = True

first = students.index(False)
students.pop(first)
second = students.index(False) + 1
print(first)
print(second)
