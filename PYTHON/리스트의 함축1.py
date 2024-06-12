# 조건식 붙이기
# if를 사용하여 조건을 추가하여 출력할 수 있다.

s = [ i for i in range(10) if i % 2 == 0 ]
print(s)

s = [ i **2 for i in range(10) if i % 2 == 0 ]
print(s)