# 리스트에서 최대값 구하기

score = [100, 80, 95 , 90 , 70]

max = score[0]   # 첫번째 요소를 최대값이라고 가정

for i in score : 
    if i > max : # 비교 후 최대값 보다 크면
        max = i  # 최대값 교체

print("최대값: %d" % max)