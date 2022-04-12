from random import *

lotto=[] #로또 번호
count=0
l_count = []
my_num = []
ok_num = []
while True:
    #5보다 작거나 같을 때 실행
    if count <= 5:
        #랜덤숫자 가져오기
        temp=randrange(1,46)
        #랜덤숫자가 lotto에 있는 리스트에 있는지 비교
        if temp not in lotto:
            #랜덤숫자 추가
            lotto.append(temp)
            count +=1
    else:
        print('6개의 번호가 추출 되었습니다.')
        break
print(lotto)
#입력 6개
my_num = []
for i in range(6):
    a = int(input("{}번째숫자를 입력하세요>>" .format(i+1)))
    my_num.append(a)
print('입력번호:',my_num)
#몇개가 맞는지 출력하시오.
for i in range(6):
    if my_num[i] in lotto:
        l_count += 1
        ok_num.append(my_num[i])

print('맞춘갯수:',l_count)
print('맞춘갯수:',ok_num)

