# 정수 두개를 입력 받아, 둘 중 작은 수 부터 큰 수 까지의 합을 출력하는 프로그램을 작성하세요. (for문 사용)


num1 = int(input("정수 입력: "))
num2 = int(input("정수 입력: "))

if num1 > num2 :
    upper = num1
    lower = num2
else :
    upper = num2
    lower = num1

sum = 0

for i in range(lower, upper+1) :
    sum += i



print(lower,"에서", upper, "까지 더하면 ", sum)