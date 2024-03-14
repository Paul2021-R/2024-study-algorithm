from itertools import permutations, combinations

heights = [int(input()) for _ in range(9)]

# 조합으로 해결하는 방법 
# for combi in combinations(heights, 7):
#   if sum(combi) == 100:
#     for height in sorted(combi):
#       print(height)
#     break
  
# 함수 + for문으로 해결하는 방법 
heights.sort()
total = sum(heights)

def f():
    for i in range(8):
        for j in range(i+1, 9):
            if (total - heights[i] - heights[j] == 100):
                for k in range(9):
                    if (i != k and j !=k):
                        print(heights[k])
                return
                # exit 을 해도 된다. 
            
f() # 함수로 빼서 기능을 1회전만 하고 나오도록 만든다. 