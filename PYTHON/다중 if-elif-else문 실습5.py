#정수 두개 입력 받아 둘 중 정수1이 큰지 작은 지 또는
#같은 지 출력하는 프로그램을 작성하세요.

num1 = int(input("정수1 입력: "))
num2 = int(input("정수2 입력: "))

if num1 > num2 :
    print("정수 1이 정수2 보다 큽니다.")
elif num1 == num2 :
    print("두 수는 같습니다.")
else :
    print("정수 2이 정수1 보다 큽니다.")