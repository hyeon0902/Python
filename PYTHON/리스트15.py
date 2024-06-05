# 리스트를 변수로 넣기

a = [1, 2, 3, 4, 5]

for i in a :
    print(i)


for i in [1, 2, 3, 4, 5] :
    print(i)

# 인덱스와 요소를 같이 출력하기

# enumerate() 함수

# for문에 담아 실행하면 리스트의 원소와 인덱스가 튜플 형태로 출력됨

num = ['one','two','three','four']

for value in enumerate(num) :
    print(value)

# 인덱스와 요소를 같이 출력하려면

num = ['one','two','three','four']

for index,value in enumerate(num) :
    print(index, value)