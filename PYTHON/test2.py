print("두 개의 정수를 입력해주세요.")

num1 = int(input("정수1 입력: "))
num2 = int(input("정수2 입력: "))

if num1 > num2 :
    num = num1 - num2
else :
    num = num2 - num1

print("두 수의 차는",num,"입니다. ")