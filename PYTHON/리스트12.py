# 다음 같이 크기 5인 리스트에 처음 요소부터 순서대로 0, 1, 2, 3, 4를
# 하나씩 추가하고, 다음과 같이 출력하는 프로그램을 작성하세요(for문 사용)

list = []

for i in range(5) :
    list.append(i)

for i in range(5) :
    print("list[%d] = %d" % (i, list[i]))