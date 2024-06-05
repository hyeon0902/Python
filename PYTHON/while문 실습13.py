# 정수 하나를 입력 받아 그 자릿수를 출력하는 프로그램을 작성해 보세요.

n = int(input("정수 입력: "))

count = 0
temp = n

while temp > 0 :
    temp = temp // 10
    count += 1

print(n, "은", count, "자리 숫자 입니다.")