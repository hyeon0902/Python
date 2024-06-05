# 다음과 같이 양의 정수를 하나 입력 받아, 그 수 만큼 3의 배수를 출력하는 프로그램을 작성하세요. (for문 사용)


num = int(input("양의 정수 입력: "))
ans = 0

for i in range(num) :
    ans += 3
    print(ans)