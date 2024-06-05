# 다음과 같이 양의 정수를 하나 입력 받아, 그 값 이하의 짝수를 오름차순으로 출력하는 프로그램을 작성하세요. (for문 사용)


# num = int(input("양의 정수 입력: "))

# for i in range(2, num+1, 2) :
#         print(i, end=" ")


num = int(input("양의 정수 입력: "))

for i in range(1, num + 1):
    if i % 2 == 0:
        print(i, end=" ")