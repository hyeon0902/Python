#정수 하나를 입력받고 그 수를 단으로 하는 구구단을 출력하세요.

dan = int(input("출력하고 싶은 단: "))

i = 1
while  i < 10 :
    print(dan, " * ", i, " = ", dan*i)
    i += 1 