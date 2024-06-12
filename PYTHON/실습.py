# 실습
# 보초값

score = []
value = 0
print("종료하려면 음수를 입력하세요")

while value >= 0 :
    value = int(input("성적 입력: "))
    if value >= 0 :
        score.append(value)

if len(score) > 0 :
    sum = sum(score)
    min = min(score)
    max = max(score)

    print("최고 점수: ", sum)
    print("최저 점수: ", min)
    print("평균 점수: ", sum/len(score))

