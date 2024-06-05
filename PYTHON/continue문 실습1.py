# while 반복문에서 continue로 코드실행 건너뛰기

i = 0
while i < 10 :
    i += 1
    if i % 2 == 0 :
        continue # 아래 코드를 실행하지 않고 건너뜀
    print(i, end=" ")