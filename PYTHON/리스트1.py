#학생이 10명이 있고 이들의 평균 성적을 계산한다고 가정하자.

score = [100,90,80,50,40,100,30,60,65,33]

sum = 0

for i in range(10) :
    sum += score[i]

print(sum)
print(sum / 10 )