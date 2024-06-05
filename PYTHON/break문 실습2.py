# for문에서 break 사용하기

for i in range(10000) : # 0부터 9999까지 반복
    print(i, end=" ")
    if i == 10 : # 특정 조건 만족하면
        break # 반복문 종료

print(end="\n")
print("반복문 탈출")