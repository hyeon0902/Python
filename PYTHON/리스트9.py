#리스트 특정 인덱스 요소 삭제

# pop(인덱스)

# 인덱스 요소를 찾아서 반환한 뒤, 해당 요소를 삭제

a = [1,2,3]
a.pop(1)

print(a)

# 인덱스를 쓰지 않으면 마지막 요소를 반환하고 삭제함.

a.pop()
print(a)