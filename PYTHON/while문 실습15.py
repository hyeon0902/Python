max = -1 # 나올 수 없는 최저값을 임시로 저장

n = int(input("양의 정수 입력: "))

while n >= 0 :
    if n > max :
        max = n
    n = int(input("양의 정수 입력: "))

if max != -1 :
    print("최대 값은 ", max, " 입니다.")