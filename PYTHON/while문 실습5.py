#다음과 같이 양의 정수를 하나 입력 받아, 그 값을 0 까지 감소시키면서 카운트 다운하는 프로그램을 작성하세요.

num = int(input("양의 정수 입력: "))

while num >= 0 :
    print(num, end=" ")
    num -= 1