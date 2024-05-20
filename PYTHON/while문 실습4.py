#다음과 같이 양의 정수를 하나 입력 받아, 1부터 그 값까지
#카운트 업 하는 프로그램을 작성하세요.

num = int(input("양의 정수 입력: "))

i = 1
while i <= num :
    print(i , end= " ")
    i += 1