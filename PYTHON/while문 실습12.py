# 정수 하나를 입력 받아 정수의 각 자리수의 합을 
# 출력하는 프로그램을 작성해 보세요.

sum = 0
n = int(input("정수 입력: "))

while n > 0 :
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("합계는", sum, "입니다.")
