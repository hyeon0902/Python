# 이전 문제를 바꾸어, 처음부터 5, 4, 3, 2, 1 을 추가하고 
# 출력하는 프로그램을 작성하세요.

list = []


for i in range(5) :
    list.append(5-i)

for i in range(5) :
    print("list[%d] = %d " % (i,list[i]))