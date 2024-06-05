#성적을 개수 제한없이 입력 받아 평균을 구하는 프로그램을 작성하세요.
#음수가 입력되면 종료되어 평균을 출력합니다.

n = 0
sum = 0
score = 0

print("종료하려면 음수를 입력하세요.")

# grade가 0이상이면 반복
# 성적을 입력 받아서 합계를 구하고 학생 수를 센다.

while score >= 0 :
    score = int(input("성적 입력: "))
    if score > 0:
        sum = sum + score
        n = n + 1

# 평균을 계산하고 화면에 출력한다.
if n > 0 :
    avg = sum / n

print("성적의 평균은 %f입니다."  %avg)