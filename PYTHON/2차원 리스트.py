# 2차원 리스트 만들기

# 리스트 안에 리스트를 넣어서 만들 수 있음
# 형식 : 리스트 = [[요소,요소],[요소,요소],[요소,요소]]

a = [[1, 2], [3, 4], [5, 6]]
print(a)

# 2차원 리스트의 요소에 접근하기
# 형식 : 리스트[세로인덱스][가로인덱스]

a = [[1, 2],
     [3, 4],
     [5, 6]]

print("a[0][0]: ", a[0][0]) # 1
print("a[2][1]: ", a[2][1]) # 6

a[1][0] = 100
print("a[1][0]: ", a[1][0]) # 3 -> 100

# 반복문 사용해서 요소 출력하기

a = [[1, 2], [3, 4], [5, 6]]

for x, y in a :
    print(x, y)

# 중첩 for 문 사용하기

a = [[1, 2], [3, 4], [5, 6]]

for i in a :                      # i 자리에 [1, 2] 이런식으로 리스트 들어감
    for j in i :
        print(j, end=' ')
    print()

#  while 문 한 번 사용하기

a = [[1, 2], [3, 4], [5, 6]]

i = 0
while i < len(a) :   # 반복할 때 리스트의 크기
    x, y = a[i]      # 요소 두개를 한꺼번에 가져오기
    print(x, y)      
    i += 1           # 인덱스를 1 증가시킴

# 중첩 while문 사용하기

a = [[1, 2], [3, 4], [5, 6]]
i = 0
while i < len(a) :                    # 세로 크기
    j = 0
    while j < len(a[i]) :             # 가로 크기
        print(a[i][j], end=' ')
        j += 1                        # 가로 인덱스를 1 증가 시킴
    print()
    i += 1                            # 세로 인덱스를 1 증가 시킴


from pprint import pprint

a = [[1, 2], [3, 4], [5, 6]]

pprint(a, indent=1, width=20)

# for 반복문을 사용

from pprint import pprint

a = [] # 빈 리스트를 생성

for i in range(3) :
    list = []                                # 안쪽 빈 리스트 생성
    for j in range(2) :
        list.append( i*2 + (j+1) )           # 안 리스트 요소 추가
        a.append(list)

pprint(a, indent=1, width=20)

# 리스트의 함축 사용

from pprint import pprint

a = [[i*2 + (j+1) for j in range(2)] for i in range(3)]

pprint(a, indent=1, width=20)

# 실습

students = [
    ['John', 80],
    ['Ian', 95],
    ['Alice', 70]
]

sum = 0
max_score = 0

for name, score in students :
    sum += score
    if(score > max_score) :
        max_score = score
        max_name = name
    
print("평균: ", sum/len(students))
print("최고 성적 학생: ", max_name)
print("최고 성적 점수: ", max_score)