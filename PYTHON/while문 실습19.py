#가위 바위 보 게임

import random

print("이길 때 까지 계속 합니다.")

win = False

while win != True :
    ans = input("가위, 바위, 보 중 하나를 선택: ")
    com = random.randint(1, 3) # 1= 가위, 2-바위, 3-보 이용
    print("컴퓨터 : ", end="")

    # 1-가위
    if com == 1 :
        print("가위")
        if ans == "가위" :
            print("비겼다.")
        elif ans == "바위" :
            print("이겼다.")
            win = True
        elif ans == "보" :
            print("졌다.")

    if com == 2 :
        print("바위")
        if ans == "가위" :
            print("졌다.")
        elif ans == "바위" :
            print("비겼다.")
        elif ans == "보" :
            print("이겼다.")
            win = True
    
    if com == 3 :
        print("보")
        if ans == "보" :
            print("비겼다")
        elif ans == "바위" :
            print("졌다.")
        elif ans == "가위" :
            print("이겼다.")
            win = True
    