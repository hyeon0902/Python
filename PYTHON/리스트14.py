# 처음부터 순서대로 0.0, 0.1 ... 1.0을 추가하여 표시하는 프로그램을 작성하세요.


list = []

for i in range(11) :
    list.append(i/10)

for i in range(11) :
    print("list[%d] = %.1f" % (i,list[i]))