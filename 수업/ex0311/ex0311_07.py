from msilib.schema import RadioButton
import random
from random import *

# lotto = []
# for i in range(0,6): #6번 반복
#     temp=randrange(1,46) #랜덤 숫자를 생성해서 temp 변수에 넣어.
#     lotto.append(temp) #temp를 한개씩 lotto에 넣기.
# print(lotto)


#로또번호 6개를 저장하여 출력하시오.



# List =[]
# for i in range(0,6):
#     a=randrange(1,46)
#     if a not in List:
#         List.append(a)
# print(List)


lotto=[]
count=0
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

Lists=[]
for i in range(0,6):
    b = randint(1,46)
    while b in Lists:
        b= randint(1,45)
    Lists.append(b)
    
print(Lists)