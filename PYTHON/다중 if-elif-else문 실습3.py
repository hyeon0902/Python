# 점수 입력 받아 학점 출력하기

score = int(input("점수 입력: "))

if score >= 90:
    print("A 학점")
elif score >= 80:
    print("B 학점")
elif score >= 70:
    print("C 학점")
elif score >= 60:
    print("D 학점")
else :
    print("F 학점")