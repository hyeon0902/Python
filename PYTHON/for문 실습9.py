#다음과 같이 정수 하나를 입력 받아 1부터 해당 숫자까지 더하는 프로그램을 작성해 보세요.

count = int(input("어디까지 계산할까요: "))
sum = 0

for i in range(count+1) :
    sum += i


print("1부터", count, " 까지의 정수의 합: ",sum)