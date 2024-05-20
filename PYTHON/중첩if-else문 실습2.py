#양수면 짝수, 홀수 출력하기

num = int(input("정수 입력: "))

if num > 0 :
    if num % 2 == 0 :
        print("짝수 입니다.")
    else :
        print("홀수 입니다.")
else :
    print("음수 입니다.")