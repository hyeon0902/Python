# 정수 두 개를 입력 받아, 둘 중 큰수에서 작은 수 사이를 카운트 다운 하는
# 프로그램을 작성하세요(for문 사용)


num1 = int(input("정수 입력: "))
num2 = int(input("정수 입력: "))

if num1 > num2 :
    upper = num1
    lower = num2
else :
    upper = num2
    lower = num1

for i in range(upper, lower-1, -1) :
    print(i)