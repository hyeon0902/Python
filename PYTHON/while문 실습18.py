#랜덤하게 구구단 문제 3개를 출력, 끝나면 몇 문제 맞는지 출력

import random

print("구구단 게임입니다.")
i = 0
score = 0

while i < 3 :
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    result = num1 * num2

    print(num1, "*", num2, "= ", end="")
    ans = int(input())

    if ans == result :
        print("맞습니다.")
        score += 1
    else :
        print("틀렸습니다.")

    i += 1

print("\n총 3문제 중", score, "문제 맞추셨습니다.")