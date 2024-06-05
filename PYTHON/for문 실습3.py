score = [90,35,75,69,80]


num = 0

for s in score :
    num += 1
    if s >= 70 :
        print(num, "번 학생 점수는",s,"이고 합격")
    else :
        print(num, "번 학생 점수는",s, "이고 불합격")