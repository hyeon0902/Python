#주사위를 계속 굴려 3이 나오면 종료하는 프로그램을 작성해 보세요.

import random

num = 0
count = 0

while num != 3 :
    num = random.randint(1,6)
    count += 1
    print("주사위를 굴렸다. ", num,"나옴")


print("드디어 3 나와서 종료합니다.")
print("종료까지 ", count, "번 입니다.")