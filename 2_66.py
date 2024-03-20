# 출력 형태 이해해보기

print("3 x 1 = 3")
print("3 x 2 = 6")
print("3 x 3 = 9")


print("2 + 5 = 7")
print("2 + 5 =", 2*5)


print("9 x 1 =", 9*1)
print("9 x 2 =", 9*2)
print("9 x 3 =", 9*3)
print("9 x 4 =", 9*4)
print("9 x 5 =", 9*5)

print(1, 2, 3)
print("Hello", "Python")

print(1, 2, 3, sep=", ") # sep에 콤마와 공백을 지정
print(4, 5, 6, sep=",")  # sep에 콤마만 지정
print("Hello", "Python", sep="") # sep에 빈 문자열을 지정
print("010", "1234", "5678", sep="-") # sep에 -를 지정

print('Hello', end=' ')
print('World', end=' ')
print('Good', end=' ')
print('Job')

print('1\n2\n3') # 문자열 안에 \n 을 사용 (줄바꿈)

print(1, 2, 3, sep='\n')