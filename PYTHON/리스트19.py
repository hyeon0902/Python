# 리스트에서 최소 값 구하기

score = [100, 80, 95, 90, 70]

min = score[0] # 첫번째 요소를 최소값이라고 가정

for i in score :
    if i < min : # 비교 후 최소값 보다 작으면
        min = i  # 최소값 교체

print("최소값: %d" % min)


score = [100, 80, 95, 90, 70]
