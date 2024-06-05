# insert(인덱스,요소)

# append, extend 는 리스트 끝에 요소를 추가

# 원하는 위치에 요소를 추가하려면 insert() 사용

a = [1,2,3]
a.insert(0, 100)

print(a)
print(len(a))

#요소 마지막에 추가하려면 a.insert(len(a), 100) 