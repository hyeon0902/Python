#아래와 같이 몇 월인지 입력받아, 그 계절을 출력하는 프로그램을 작성하세요.

month = int(input("몇 월입니까: "))

if (month >= 3 and month <= 5) :
    print("봄 입니다.")
elif (month >= 6 and month <= 8) :
    print("여름 입니다.")
elif (month >= 9 and month <= 11) :
    print("가을 입니다.")
elif (month == 1 or month == 2 or month == 12) :
    print("겨울 입니다.")
else :
    print("그런 월은 없습니다.")
