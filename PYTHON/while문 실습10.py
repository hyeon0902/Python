# 누적합 구하기

n = int(input("양의 정수 입력: "))

i = 1
sum = 0

while i <= n :
    sum = sum + i
    i += 1

print("1부터", n, "까지의 합은", sum, "입니다.")