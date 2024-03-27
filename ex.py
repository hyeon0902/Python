# a,b = map(int, input().split())
# print(a+b)



# c = int(input())

# d = int(input())

# print(c+d)

# a,b = map(int, input().split())

# print(a-b)

# a,b = map(int, input().split())

# if a < b :
#     print("<")
# elif a > b :
#     print(">")
# elif a == b :
#     print("==")

# 두 자연수 A와 B가 주어진다. 

# 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
    
# a = 7
# b = 3

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# dan = int(input())

# while dan < 10 :
#     print(dan, "단")
#     for i in range(1,10):
#         print(dan, "*", i, "=", dan*i)
#     print()

# dan = int(input())
# for i in range(1,10):
#     print(dan,"*",i,"=",dan*i)

# while True:
#     try:
#         a,b = map(int, input().split())
#         print(a + b)
#     except EOFError:
#         break

# x = map(int, input().split())

# a = [1, 10, 4 , 9 ,2 ,3 ,8 ,5 ,7 ,6]

# for i in a :
#     if i < x :
#         print(i,end=" ")

print(1,2,3, sep= '\n')
print(1,2,3, end="")
print(1,2,3, sep="\t")
print('hello'); print('world')
print('hello', end=" "); print('wolrd')

print(15+37)

print("15에서 37을 뺀 값은", 15-37 ,"입니다.")

print("동","서","남","북", sep="\n")

#변수에 정수값을 대입하고 표시

number = 75

print("no 의 값은", number, "입니다.")

year = 2021
month = 10
day = 31
hour = 11
minute = 29
secend = 42

print(year,month,day,sep="/",end=" ")
print(hour,minute,secend,sep=":")