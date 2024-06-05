#리스트 요소 추가

a = [1, 2, 3]
print(a)

a.append(40)
print(a)

b = []

b.append(10)
print(b)

#append(리스트)

a = [1,2,3]
a.append([40,50])

print(a)      # [1,2,3,[40,50]]
print(len(a)) # 4