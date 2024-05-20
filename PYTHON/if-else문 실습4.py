#아래와 같이 정수 두개를 입력 받아 둘 중에 두 수의 차를 출력하는 프로그램을 작성하세요.

num1 = int(input("정수1 입력: "))
num2 = int(input("정수2 입력: "))

if num1 > num2 :
    ans = num1 - num2
else :
    ans = num2 - num1
    
print("두 수의 차는 ", ans , " 입니다.")