# 5명의 성적을 입력받고, 성적을 모두 출력하는 프로그램을 작성하세요

student = 5

score = []

for i in range(student) :
    value = int(input("성적 입력: "))
    score.append(value)

for i in range(student) :
    print("%d 번째 성적: %d" % (i+1,score[i]))
