data = 'hello world!'

print(data)

a = "Hello"
b = "World!"
print(a + " " + b) # 문자열 연산

print(a * 3) # 곱하기도 되구요 ~ ~

c = "Hello World!Hello World!Hello World!"
print(c[len(data):len(data) + len(data)]) # 슬라이스도 됩니다. 

#dictionary 
dic_a = dict()
dic_a['apple'] = '사과'
dic_a['banana'] = '바나나'
dic_a['coconut'] = '코코넛'

print(dic_a)

if 'apple' in dic_a:
  print("true")
else:
  print("false")

# 키 값 가져오기 
print(dic_a['apple'])
key_list = dic_a.keys()
value_list = dic_a.values()
print(key_list)
print(value_list)
print ("dictionary id : ", id(dic_a))
print("key_list id : ", id(key_list))
print("value_list id : ", id(value_list))

for key in key_list:
	print(dic_a[key])

a = set([1, 2, 3, 4, 5, 6, 6])
print(a) 
b = {6, 7, 8, 1, 0}
print(b)

print(a | b)
print (a & b)
print(a - b)

c = a - b
print (c)
c.add(10)
print (c) 
c.update([11, 14, 20])
print(c)
c.remove(14)
print(c)