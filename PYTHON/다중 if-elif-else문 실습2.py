#점수를 입력 받아 70점 이상이면 합격, 
#50점 이상이면 재시, 
#그 이하 불합격을 출력하세요.

score = int(input("점수 입력: "))

if score >= 70 :
    print("합격")
elif score >= 50 :
    print("재시")
else :
    print("불합격")