#중첩 for문을 사용하여 2단부터 9단까지를 모두 출력하세요.


for i in range(2, 10) :
    for j in range(1, 10) :
        print(i,"*",j,"=",i*j)
    print()