#구구단 해당 단을 반복문으로 출력하는 프로그램을 작성해 보세요.

dan= int(input("단: "))

for i in range(1,10) :
    sum = dan * i
    print(dan, " * ", i, " = ", sum)