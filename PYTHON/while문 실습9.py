num1 = int(input("정수 입력: "))
num2 = int(input("정수 입력: "))



if num1 > num2 :
    upper = num1
    lower = num2
else :
    upper = num2
    lower = num1

i = upper

while i >= lower :
    print(i)
    i -= 1