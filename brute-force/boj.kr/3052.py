import sys

basket = set()

for _ in range(10):
   basket.add(int(sys.stdin.readline()) % 42)

print(len(basket))