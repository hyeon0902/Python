# step을 음수로 하는 방법 말고 reversed() 함수를
# 사용하는 방법도 있음


range(3) # 0,1,2 가 생성됨
reversed(range(3)) # 2,1,0 으로 순서 뒤집음

for i in reversed(range(3)) :
    print(i, end=" ")