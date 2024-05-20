#정수 입력받아 양수,음수 아니면 0 출력하는 프로그램 작성

num = int(input("정수 입력: "))

if num > 0 :
    print(num, " 은 양수 입니다.")
elif num < 0 :
    print(num, " 은 음수 입니다.")
elif num == 0 :
    print(num, " 입니다.")
