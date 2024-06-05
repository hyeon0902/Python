# while 반복문으로 요소 출력하기

# while문으로 요소 출력하려면 인덱스로 요소값을 하나씩 접근 해야한다.

a = [1, 2, 3, 4, 5]

i = 0
while i < len(a) :
    print(a[i])
    i += 1