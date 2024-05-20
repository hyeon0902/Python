#나이, 점수로 출력

age = int(input("나이 입력: "))

if age >= 20 :
    print("응시 가능")
    score = int(input("점수 입력: "))
    if score >= 80 :
        print("합격")
    else :
        print("불합격")
else :
    print("응시 불가능")