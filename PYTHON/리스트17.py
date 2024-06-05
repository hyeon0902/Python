# 지난 챕터의 성적 리스트 처리 수정


score = [100, 80, 95, 90, 70]

sum = 0

for i in score :
    sum += i

print('성적합계: %d' %sum)
print('성적평균: %.1f' %(sum/5))


score = [100, 80, 95, 90, 70]

i = 0
sum = 0

while i < len(score) :
    sum += score[i]
    i += 1

print('성적합계: %d' % sum)
print('성적평균: %.1f' % (sum/len(score)))