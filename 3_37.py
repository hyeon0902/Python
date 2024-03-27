# name = input("이름이 무엇인가요? ")
# print("만나서 반갑습니다. " + name + "씨!")
# age = input( "몇 살인가요? ")
# print("네, 그러면 당신은 " + age + " 살이시군요, " + name + "씨!")


# x = input("첫 번째 정수: ")
# y = input("두 번째 정수: ")

# sum = x + y 
# print("합은 ", sum)

# x = int(input("첫 번째 정수: "))
# y = int(input("두 번째 정수: "))

# sum = x + y
# print("합은 ", sum)


# no = int(input("no의 값을 입력해주세요 : "))
# print("no의 값은 ", no , "입니다.")

# a = int(input("정수를 입력해주세요 :"))
# print("이 값에서 10을 빼면", a-10, "입니다.")

# print("두 개의 정수를 입력해주세요.")
# a = int(input("정수1 : "))
# b = int(input("정수2 : "))
# print("이들의 곱은", a*b , "입니다.")

# print("세 개의 정수를 입력해주세요.")
# a = int(input("정수1 : "))
# b = int(input("정수2 : "))
# c = int(input("정수3 : "))
# sum = a+b+c
# print("이들의 합은", sum, "입니다.")

# # 사각형의 가로 길이
# width = 10

# # 사각형의 세로 길이
# height = 20

# # 사각형의 면적 계산
# area = width * height

a = 1
b = 10

if a == b :
    print("a와 b는 동일하다.")
elif a > b :
    print("a가 b보다 크다")
elif a < b :
    print("a가 b보다 작다.")

a = 10
if a == 10:
    print("a는", a, "입니다.")

print("끝")

#첫번쨰 선언 s 
s = "hello" \
    + " world"

# 두번쨰 재선언 s 위에껀 초기화
s = ("Hello" 
    + " World")
print(s)


def plus(x, y,z) :
    return x+y+z

a = plus(10,20,30)
print("a==>", a)

b = plus(50,20,30)
print("b==>", b)

c = plus(100,100,100)
print("c==>", c)
