#성별을 입력받아, 남자면 몸무게를 입력 받고 70kg이상이면 '농구',미만은'축구'를 추천하고, 여자면 키160cm이상이면 '배구',미만은 '피구'를 추천하세요.

print("********************************************")
print("성별과 몸무게, 키에 따른 운동경기 추천 프로그램")
gender = input("성별 입력[남자/여자]: ")

if gender == "남자" :
    weight = int(input("몸무게 입력(kg): "))
    if weight >= 70 :
        print("[농구] 경기를 추천합니다.")
    else :
        print("[축구] 경기를 추천합니다.")
else : 
    height = float(input("키 입력(cm): "))
    if height >= 160 :
        print("[배구] 경기를 추천합니다.")
    else :
        print("[피구] 경기를 추천합니다.")


